import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

private_key_path = 'private.pem'
encrypted_key_file = 'email.txt'
output_file = 'putmeondesktop.txt'

def decrypt_key_with_private_key(private_key_path, encrypted_key_file):
    with open(private_key_path, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    
    with open(encrypted_key_file, 'rb') as file:
        encrypted_key = file.read()
    
    decrypted_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    return decrypted_key

decrypted_key = decrypt_key_with_private_key(private_key_path, encrypted_key_file)

with open(output_file, 'w') as file:
    file.write(decrypted_key.decode())  

print("Decrypted key has been written to 'putmeondesktop.txt' on the desktop.")
