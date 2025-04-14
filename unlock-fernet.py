import os
from cryptography.fernet import Fernet

# Fungsi untuk memuat kunci enkripsi dari file
def load_key():
    return open("secret.key", "rb").read()

# Fungsi untuk mendekripsi file
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    # Menghapus ekstensi .TomwareENC dan menyimpan file hasil dekripsi
    decrypted_file_path = file_path.replace('.TomwareENC', '')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"File '{file_path}' telah didekripsi menjadi '{decrypted_file_path}'.")

# Fungsi untuk mendekripsi seluruh file dalam folder Downloads
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.TomwareENC'):  # hanya mendekripsi file yang memiliki ekstensi .TomwareENC
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)

# Muat kunci enkripsi
key = load_key()

# Folder tempat file yang ingin didekripsi, misalnya 'Download'
folder_to_decrypt = "/storage/emulated/0/targetRS"  # Path folder download pada Android

# Mulai dekripsi semua file dalam folder
decrypt_folder(folder_to_decrypt, key)
