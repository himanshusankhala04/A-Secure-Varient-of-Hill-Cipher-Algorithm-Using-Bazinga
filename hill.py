from KeyGenerator import randomgen as re
import numpy as np
from egcd import egcd

characters, letter2index , index2letter = re.dictGen()


def encrypt(message, K):
    encrypted = ""
    list_message = []

    #for char to number convertion
    for char in message:
        list_message.append(letter2index[char])

    #spliting message as per key length
    divided_message = [list_message[i : i + int(K.shape[0])] for i in range(0, len(list_message), int(K.shape[0]))]

    #klen * 1 matrix creation
    for P in divided_message:
        P = np.transpose(np.asarray(P))[:, np.newaxis]
        #for odd length
        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter2index[" "])[:, np.newaxis]

        # encryption
        numbers = np.dot(K, P) % len(characters)

        n = numbers.shape[0]  #for length of encrypted message

        #Map back to get in char
        for i in range(n):
            number = int(numbers[i, 0])
            encrypted += index2letter[number]

    return encrypted


def decrypt(cipher, Kinv):
    decrypted = ""
    cipher_matrix = [] #cipher text to number

    for letter in cipher:
        cipher_matrix.append(letter2index[letter])

    #spliting message as per key length
    divided_message = [ cipher_matrix[i : i + int(Kinv.shape[0])] for i in range(0, len(cipher_matrix), int(Kinv.shape[0])) ]

    #klen * 1 matrix creation
    for C in divided_message:
        C = np.transpose(np.asarray(C))[:, np.newaxis]

        # decryptiion
        numbers = np.dot(Kinv, C) % len(characters)

        n = numbers.shape[0]

        #Map back to get in char
        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index2letter[number]

    return decrypted
