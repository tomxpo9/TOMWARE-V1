import os
from cryptography.fernet import Fernet
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Function to load encryption key from file
def load_key():
    return open("secret.key", "rb").read()

# Function to decrypt a file and remove the encrypted file
def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        # Remove the .TomwareENC extension and restore the original file
        original_file_path = file_path.rsplit('.TomwareENC', 1)[0]
        with open(original_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        # Remove the encrypted file after decryption
        os.remove(file_path)

        print(Fore.GREEN + f"[✓] '{file_path}' has been decrypted and restored to '{original_file_path}'. The encrypted file has been deleted.")
    except Exception as e:
        print(Fore.RED + f"[!] Failed to decrypt '{file_path}': {e}")

# Function to decrypt all files in a folder
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Only decrypt files with .TomwareENC extension
            if file_path.endswith('.TomwareENC'):
                decrypt_file(file_path, key)

# Run decryption process
if __name__ == "__main__":
    # Load the encryption key
    key = load_key()

    # Folder to decrypt (adjust path as needed)
    folder_to_decrypt = "/storage/emulated/0/targetRS"  # Path to folder on Android

    # Start the decryption process
    decrypt_folder(folder_to_decrypt, key)
