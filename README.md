# ✨ Stylish QR Code Generator ✨

A user-friendly web application built with Streamlit that allows you to create, customize, and download QR codes in real-time. Go beyond boring black-and-white squares and design QR codes that match your style!

### 🔗 Live Demo

[**>> Click here to try the app live! <<**](https://qr-codegen.streamlit.app/)

### 🚀 Features

- **Instant QR Code Generation**: Enter any URL and get a QR code instantly.

- **Live Preview**: See your QR code update in real-time as you tweak the settings.

- **🎨 Advanced Customization**:

  - **Color Picker**: Choose custom foreground (dot) and background colors.

  - **Box Size**: Control the pixel size of each module in the QR code for higher or lower resolution.

  - **Border Control**: Adjust the thickness of the white space (quiet zone) around the QR code.

- **📥 One-Click Download**: Download your final creation as a high-quality PNG file with a sensible filename.

- **Sleek & Responsive UI**: A clean, modern interface that works beautifully on both desktop and mobile devices.

- **Stateful Design**: Uses Streamlit's session state to remember your design even if you interact with other parts of the app.

### 📸 Screenshot

![alt text](image.png)

### 🛠️ Tech Stack

- **Framework**: [Streamlit](https://streamlit.io/) - For building and deploying the web application.

- **QR Code Logic**: [qrcode](https://pypi.org/project/qrcode/) - The core library for generating the QR codes.

- **Image Handling**: [Pillow (PIL)](https://pypi.org/project/Pillow/) - For processing and handling the generated image data.

- **Language**: Python 3
