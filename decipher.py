#encrypt and decrypt texts + print output of either
def encrypt(text, shift):
    text = text.lower()
    encrypted_text = ""
    for char in text:
        if char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    text = text.lower()
    decrypted_text = ""
    for char in text:
        if char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

secret = ""
print(decrypt(secret, 3))