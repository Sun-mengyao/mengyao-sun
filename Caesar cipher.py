def caesar_encrypt(text, shift):
    char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""
    for char in text:
        char = char.upper()
        if char in char_set:
            index = char_set.index(char)
            new_index = (index + shift) % len(char_set)
            encrypted_text += char_set[new_index]
        else:
            encrypted_text += char
    return encrypted_text

plaintext = "DC94"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)
print(f"plaintext: {plaintext}")
print(f"ciphertext: {ciphertext}")
