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


plaintext = "GFC7"
key = [2, 1, 4, 3]
ciphertext = encrypt(plaintext, key)
print(f"plaintext: {plaintext}")
print(f"ciphertext: {ciphertext}")

