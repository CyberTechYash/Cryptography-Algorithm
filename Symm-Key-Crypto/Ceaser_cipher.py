def encrypt(plaintext, shiftkey):
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        ciphertext += chr((ord(char) + shiftkey - 65) % 26 +65)
    return ciphertext

def decrypt(ct, shiftkey):
    pt = ""
    for i in range(len(ct)):
        char = ct[i]
        pt += chr((ord(char) - shiftkey - 65) % 26 +65)
    return pt

plaintext = "yash"
shiftkey = 2
print(plaintext)
ct = encrypt(plaintext.upper(), shiftkey)
print(ct)
a = decrypt(ct, shiftkey)
print(a.lower())