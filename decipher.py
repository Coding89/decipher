#encrypt + decrypt texts + print output of either
# encrypt text on line 5 in the ""
def encrypt(text, shift):
    text = text.lower()
    encrypted_text = ""
    for char in text:
        if char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text
# decrypt text on line 15 in the ""
def decrypt(text, shift):
    text = text.lower()
    decrypted_text = ""
    for char in text:
        if char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":

    secret = ""
    print(decrypt(secret, 3))