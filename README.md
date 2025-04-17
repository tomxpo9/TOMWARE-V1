# TOMWARE-V1

**TOMWARE-V1** is a Python tool that provides encryption and decryption of files using the **Fernet** encryption algorithm from the `cryptography` library. This tool is designed to be cross-platform and can also be executed via USB Rubber Ducky or Pico Ducky with the help of a Ducky Script (`payload.dd`).

## Features

- Encrypt and decrypt files using secure Fernet encryption
- Works on all major operating systems: Windows, Linux, macOS, and Android (via Termux) with python already installed.
- Can be triggered via USB Rubber Ducky / Pico Ducky for automated execution. Select the specify payload.dd depending what is your OS target.

## File Descriptions

- `lock-fernet.py` – Encrypts all files in target folders. You can change the folder directories as you.
- `unlock-fernet.py` – Decrypts a previously encrypted folders file.
- `payload.dd` – Ducky Script for executing `lock-fernet.py` using USB Rubber Ducky / Pico Ducky if you used usb hid like USB RUBBER DUCKY by hak5 Or PICO DUCKY by dbisu.
- `README.md` – Documentation
- `LICENSE` – MIT License

## Prerequisites

- Python 3.x installed on the target machine
- `cryptography` library (install using `pip install cryptography colorama lolcat`)
- Or using 'apt install python-cryptography' if theres was an error while using pip install cryptograpy
