def encrypt(plaintext, key):

    ciphertext = ''

    # Loop melalui setiap karakter dalam plaintext
    for i in range(len(plaintext)):
        # Operasi XOR 
        encrypted_char = chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
        # hello = chr(ord(plaintext[i]))
        # hello2 =  ord(key[i % len(key)])
        ciphertext += encrypted_char

    return ciphertext

def decrypt(ciphertext, key):
    return encrypt(ciphertext, key)

plaintext = input("Masukkan Text: ")
key = input("Masukkan Key: ")

# Enkripsi
encrypted_text = encrypt(plaintext, key)
print("Ciphertext:", encrypted_text)

# Dekripsi
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
