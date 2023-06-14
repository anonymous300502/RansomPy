# RansomPy
A ransomware which fully encrypts the target system and then encrypts the key itself, The key can only be decrypted by the attacker. It also starts a timer and displays a ransom note which cannot be closed. If timer runs out, all encrypted files are permanently deleted.
# Ransomware Program

This is a ransomware program developed using Python. It encrypts files on the victim's computer and demands a ransom to decrypt them.

## Disclaimer

**Please note that this program is for educational purposes only** and should not be used for any malicious activities. The primary goal of this README is to explain the functionality of the program and provide information about the imported modules and functions used in the code.

## Modules Used

The program utilizes the following Python modules:

- os: Provides a way to interact with the operating system, perform file operations, etc.
- time: Enables time-related operations such as delays and timestamps.
- queue: Implements a queue data structure for message passing between threads.
- ctypes: Allows calling functions from dynamic link libraries/shared libraries.
- shutil: Provides high-level file operations such as copying and deleting.
- win32gui: Offers access to Windows GUI functions for managing windows.
- platform: Provides information about the underlying platform (e.g., Windows or Linux).
- pyfiglet: Allows generating ASCII art from text.
- threading: Enables multi-threading for concurrent execution.
- subprocess: Allows spawning new processes, interacting with system commands.
- urllib.request: Provides functionality to retrieve data from URLs.
- countdowntimer: A custom module for displaying countdown timer windows.
- datetime: Provides date and time manipulation functions.
- wintypes: Defines Windows-specific types for ctypes.
- termcolor: Enables colored output in the terminal.
- cryptography: A library for encryption and decryption operations.

## Functions

The program defines the following functions:

- `delete_folders(folders)`: Deletes specified folders and their contents after a countdown timer reaches zero.
- `generate_key()`: Generates a symmetric encryption key using the Fernet algorithm.
- `encrypt_file(file_path, key)`: Encrypts a file using the specified encryption key.
- `decrypt_file(file_path, key)`: Decrypts a file using the specified encryption key.
- `encrypt_folders(folders, key)`: Encrypts files within the specified folders using the encryption key.
- `decrypt_folders(folders, key)`: Decrypts files within the specified folders using the encryption key.
- `change_desktop_background(image_url, desktop_path)`: Changes the desktop background image.
- `create_ransom_note(desktop_path)`: Creates a ransom note file on the victim's desktop.
- `show_ransom_note()`: Displays the ransom note file and ensures it remains the active window.
- `get_available_drives()`: Retrieves a list of available disk drives.
- `get_folders_to_encrypt(drives, desktop_path)`: Determines the folders to encrypt based on the available drives.
- `encrypt_key_with_public_key(key)`: Encrypts the encryption key with a public key.
- `wait_for_decrypted_key()`: Waits for a decrypted key file and decrypts the folders.

## Usage and Execution

1. **Disclaimer**: Again, please note that this program is for educational purposes only and should not be used for any malicious activities.

2. **Execution**: Run the program using Python. Make sure you have the required modules installed.

3. **Behavior**: The program will encrypt files within specified folders, change the desktop background, and display a ransom note with instructions for file decryption.

4. **Decryption**: To decrypt the files, follow the instructions in the ransom note. The program will wait for a decrypted key file and use it to decrypt the folders.

## Important Note

Please refrain from using this code for any malicious purposes. It is essential to respect the privacy and security of others.
