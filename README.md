# 📱 Mobile Touchpad
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**Mobile Touchpad** is a Python-based server-client application that turns your smartphone into a wireless touchpad and keyboard for your computer. It leverages Flask-SocketIO, PyAutoGUI, and QR code-based pairing to offer a seamless, cross-platform remote control experience over Wi-Fi.

---

## 🚀 Features

- 🖱️ Use your phone as a **mouse touchpad**  
- 🧭 Multi-touch gestures: **left-click**, **right-click**, **scrolling**, **dragging**  
- 🌐 Connect easily with **QR code pairing**  
- ⚡ Real-time interaction over **WebSockets**

---

## 📦 Tech Stack

**Backend**: Python, Flask, Flask-SocketIO, PyAutoGUI, Tkinter, qrcode  
**Frontend**: HTML, CSS, JavaScript

---

## 📥 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/HiPrabel/Mobile-Touchpad.git
   ```
2. Navigate into the project directory:
   ```sh
   cd Mobile-Touchpad
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Running the server:
   ```sh
   python main.py
   ```

- A **QR code** will appear. Scan it from your mobile browser to start using your phone as a touchpad.

---

## 📱 Client Setup (Phone Side)

### ✅ Requirements

- Mobile browser (Chrome, Brave, etc.)
- Both phone and computer must be connected to the **same Wi-Fi network**

### 🔗 How to Use

1. Start the server on your PC  
2. Scan the QR code with your phone  
3. Use the touch area as a **mousepad**

---

## 🧠 Touchpad Gestures

| Action         | Gesture                               |
|----------------|---------------------------------------|
| Move cursor    | Slide one finger                      |
| Left-click     | Single tap                            |
| Right-click    | Two-finger tap                        |
| Scroll         | Two-finger drag up/down               |
| Drag and Drop  | Double-tap and hold, then drag        |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! Whether it's a new feature or bug fix, feel free to contribute.

---

## Contact

For questions or support, please reach out at **Prabel Pandey** - [GitHub](https://github.com/HiPrabel) [prabel397@gmail.com]
