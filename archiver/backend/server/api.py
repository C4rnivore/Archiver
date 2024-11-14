from .huffman import encrypt_data, decrypt_data

def encrypt(input:bytes):
    res = encrypt_data(input.decode())
    with open('Encoded.txt', 'w') as f:
        f.write(res)
        f.close()
    return 

def decrypt(input:bytes):
    res = decrypt_data(input.decode())
    with open('Decoded.txt', 'w') as f:
        f.write(res)
        f.close()
    return 


