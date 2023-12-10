from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Protocol.KDF import PBKDF2

import textwrap

def decrypt_file(encrypted_file_path, password):
    with open(encrypted_file_path, 'rb') as file:
        ciphertext_iv = file.read()

    iv = ciphertext_iv[-AES.block_size:]
    ciphertext = ciphertext_iv[:-AES.block_size]

    passwd = textwrap.dedent(password)[:-1]
    salt = b'salt123'
    key = PBKDF2(passwd.encode(), salt, dkLen=16)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)

    decrypted_file_path = encrypted_file_path[:-4]  # remove the '.enc' extension
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_data)

    print("Decryption successful. Decrypted file saved as:", decrypted_file_path)

# Example usage:
password = "ni5h2h?Yrq8Do?n+|6a;pKbZkv%}O~tV" 
encrypted_file_path = "./flag.txt.enc"
decrypt_file(encrypted_file_path, password)
