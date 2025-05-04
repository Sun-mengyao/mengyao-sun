import numpy as np

def caesar_decrypt(text, shift):
    char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_text = ""
    for char in text:
        char = char.upper()
        if char in char_set:
            index = char_set.index(char)
            new_index = (index - shift) % len(char_set)
            decrypted_text += char_set[new_index]
        else:
            decrypted_text += char
    return decrypted_text

def create_permutation_matrix(key):
    n = len(key)
    P = np.zeros((n, n), dtype=int)
    for i in range(n):
        P[i][key[i] - 1] = 1
    return P

def permutation_decrypt(ciphertext, key):
    P = create_permutation_matrix(key)
    cipher_vector = np.array([ord(c) for c in ciphertext])
    P_T = P.T
    plain_vector = np.dot(P_T, cipher_vector)
    plaintext = ''.join([chr(int(c)) for c in plain_vector])
    return plaintext

def combined_decrypt(ciphertext, caesar_shift, permutation_key):
    permutation_decrypted = permutation_decrypt(ciphertext, permutation_key)
    caesar_decrypted = caesar_decrypt(permutation_decrypted, caesar_shift)
    return caesar_decrypted

ciphertext = "FG7C"
caesar_shift = 3
permutation_key = [2, 1, 4, 3]
decrypted_text = combined_decrypt(ciphertext, caesar_shift, permutation_key)
print(f"decrypted plaintext: {decrypted_text}")
