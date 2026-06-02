"""
Caesar Cipher Module
Provides functions to encrypt and decrypt text.

The first part "encrypt" forces a string to lowercase, then shifts letters forward in the English alphabet with no impact 
on non-alphabet characters such as numerals.

The second part "decrypt" forces a string to lowercase, then shifts letters backward in the English alphabet with no impact on non-alphabet characters.
"""
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

if __name__ == "__main__":
#Example execution: decrypt a secret message with a shift key of 3
    secret = ""
#Change the "decrypt" to "encrypt" if you want to encrypt the text.
    print(decrypt(secret, 3))