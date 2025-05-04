import numpy as np


def create_permutation_matrix(key):
    n = len(key)
    P = np.zeros((n, n), dtype=int)
    for i in range(n):
        P[i][key[i] - 1] = 1
    return P


def encrypt(plaintext, key):
    P = create_permutation_matrix(key)
    plain_vector = np.array([ord(c) for c in plaintext])
    cipher_vector = np.dot(P, plain_vector)
    ciphertext = ''.join([chr(int(c)) for c in cipher_vector])
    return ciphertext


def decrypt(ciphertext, key):
    P = create_permutation_matrix(key)
    cipher_vector = np.array([ord(c) for c in ciphertext])
    P_T = P.T
    plain_vector = np.dot(P_T, cipher_vector)
    plaintext = ''.join([chr(int(c)) for c in plain_vector])
    return plaintext


plaintext = "2025"
key = [4, 1, 2, 3]
ciphertext = encrypt(plaintext, key)
print(f"plaintext: {plaintext}")
print(f"ciphertext: {ciphertext}")
decrypted_text = decrypt(ciphertext, key)
print(f"decrypted plaintext: {decrypted_text}")
