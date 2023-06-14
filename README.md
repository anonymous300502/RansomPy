# RansomPy
A ransomware which fully encrypts the target system and then encrypts the key itself, The key can only be decrypted by the attacker. It also starts a timer and displays a ransom note which cannot be closed. If timer runs out, all encrypted files are permanently deleted.
# Ransomware Program

This is a ransomware program developed using Python. It encrypts files on the victim's computer and demands a ransom to decrypt them.

## Disclaimer

**Please note that this program is for educational purposes only** and should not be used for any malicious activities. The primary goal of this README is to explain the functionality of the program and provide information about the imported modules and functions used in the code.
The Developers will not be liable to any damage caused by the unethical use of this code. 

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

2. **Execution**: Use Pyinstaller to make a .exe using the ransomware.py as the base file, create a windowed terminal if needed(recommended).

3. **Real-Life Scenario**: - Attacker creates public/private keys from attackerkeys.py and adds his public key in the main code and send the malware to the target.
                           - Once the target system gets encrypted a file called 'email.txt' containing the encrypted key will appear on it's desktop.
                           - The target will pay the ransom and then only send the file to the attacker. 
                           - The attacker will decrypt the key using decrypt_fernetkey.py and send a file 'putmeondesktop.txt' containing decrypted key to the target
                           - The target will have to place the file on it's desktop and then wait for the decryption process to complete.
                           - The code will stop once decryption is completed, or if the target fails to pay the ransom the code will delete all the files once the countdown ends and exits.

4. **Behavior**: When someone opens this .exe, The program will encrypt files within their drives, leaving important folders for windows functioning such as system32, Then it will display a ransom note.
                 A countdown timer opens up displaying a 24 hour countdown and the program starts waiting for a file 'putmeondesktop'.txt on the desktop and once recieved it will decrypt all the folders. If, however, the target fails to get the decrypted key all the files will be permanently deleted once the timer runs out.

5. **Decryption**: To decrypt the files, follow the instructions in the ransom note. The program will wait for a decrypted key file and use it to decrypt the folders.

## Contributors
1. [Abhishek Sharma] (https://github.com/anonymous300502)
2. [Manaswi Sharma] (https://github.com/manaswii)
