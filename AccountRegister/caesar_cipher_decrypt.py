def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text += chr(shifted)
            elif char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = "YBBC ANFGL HAQRE GJB"

# Try all possible shifts (1 to 25) to find the correct decryption
possible_decryptions = {}
for shift in range(1, 26):
    possible_decryptions[shift] = caesar_cipher_decrypt(ciphertext, shift)

print(possible_decryptions)

