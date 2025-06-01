from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, emit
from engineio.async_drivers import gevent
import pyautogui
import qrcode
import socket
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import pystray
from pystray import MenuItem as Item
from multiprocessing import Process, freeze_support
import os, sys
import mimetypes
import multiprocessing

server_process = None

# Flask setup
mimetypes.add_type('application/javascript', '.js')
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  
socketio = SocketIO(app, async_mode='gevent')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def custom_static(filename):
    if filename.endswith('.js'):
        mimetype = 'application/javascript'
    else:
        mimetype = None 
    return send_from_directory('static', filename, mimetype=mimetype)

@socketio.on('mousemove')
def handle_mousemove(data):
    dx = data['dx']
    dy = data['dy']
    #print(f'Moving: dx: {dx}, dy: {dy}')
    x, y = pyautogui.position()
    pyautogui.moveTo(x + dx, y + dy, _pause=False)

@socketio.on('scroll')
def handle_scroll(data):
    dy = int(data['dy'])  # convert dy to integer
    pyautogui.scroll(dy, _pause=False)

@socketio.on('mousedown')
def handle_mousedown():
    print('Mouse down')
    pyautogui.mouseDown(_pause=False)

@socketio.on('mouseup')
def handle_mouseup():
    print('Mouse up')
    pyautogui.mouseUp(_pause=False)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to an arbitrary address to get the local IP
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def run_server():
    socketio.run(app, host='0.0.0.0', port=48080)

def start_server():
    global server_process
    server_process = Process(target=run_server)
    server_process.start()

# Pystray setup
def quit_action(icon, item):
    global server_process
    if server_process is not None:
        server_process.terminate()
    icon.stop()
    root.quit()
    root.destroy()

# Pystray setup
def open_action(icon, item):
    def deiconify_and_focus():
        root.wm_deiconify()
        root.focus_force()

    icon.stop()
    root.after(100, deiconify_and_focus)

def hide_window():
    root.withdraw()
    menu=pystray.Menu(Item('Open', open_action, default=True), Item('Quit', quit_action))
    icon=pystray.Icon('MobileTouchPad', 'logo512', menu, on_click=open_action)
    icon.run()

def disconnect():
    socketio.server.disconnect() 
    return 'Disconnected'

def on_quit(icon):
    icon.stop()

if __name__ == '__main__':
    multiprocessing.freeze_support()

    root = tk.Tk()
    root.title('MobileTouchPad Server')
    root.geometry('400x400')  # Set the window size

    # labels
    local_ip = get_local_ip()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(f'http://{local_ip}:48080')
    qr.make(fit=True)
    server_address_label = tk.Label(root, font=('Arial', 18))
    server_address_label.config(text=f'Server address:')
    server_address_label.pack(anchor='w')

    server_ip_entry = tk.Entry(root, width=50, font=('Arial', 18))
    server_ip_entry.insert(0, f'http://{local_ip}:48080')
    server_ip_entry.configure(state='readonly')
    server_ip_entry.pack(anchor='w')

    qr_code_label = tk.Label(root)
    qr_code_label.pack()

    # Generate QR code image
    img = qr.make_image(fill='black', back_color='white')
    bio = BytesIO()
    img.save(bio, format='PNG')
    qr_img = ImageTk.PhotoImage(Image.open(bio))

    # Update QR 
    qr_code_label.config(image=qr_img)
    qr_code_label.image = qr_img  # keep a reference to the image

    # Override the Tkinter close window event
    root.protocol('WM_DELETE_WINDOW', hide_window)

    # Start the server when the Tkinter window is created
    root.after(0, start_server)

    # Start the application
    root.mainloop()
    root.destroy()
    