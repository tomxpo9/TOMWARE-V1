# Fernet Folder Encryptor (Pico Ducky Compatible)

A simple Python script that encrypts all files within a specified folder using the **Fernet** symmetric encryption from the `cryptography` library.

> **Disclaimer**:  
> This script is **not** ransomware and is **not intended for malicious use**. It is designed strictly for educational purposes, personal data protection, or ethical cybersecurity experiments.

## Features

- Encrypts all files in a user-selected folder.
- Automatically generates a Fernet key and saves it to a `.key` file.
- Supports decryption with the same key.
- Compatible with text files, images, documents, etc. (excluding subfolders).
- Can be executed via **Pico Ducky** (Raspberry Pi Pico running as a USB HID device).

## Pico Ducky Usage

This script is designed to be triggered using a **Pico Ducky** device. For example, the Pico can simulate keystrokes to:

- Open a terminal or command prompt.
- Download and execute the encryption script from a remote source or USB storage.
- Optionally run the script silently.

> This is intended for red team demos, ethical hacking labs, or secure automation only.

## Requirements

- Python 3.x
- `cryptography` library

Install:
```bash
pip install cryptography OR apt install python-cryptography 
