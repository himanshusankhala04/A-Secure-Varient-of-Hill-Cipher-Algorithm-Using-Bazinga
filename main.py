import math
import hill as h
from KeyGenerator import randomgen as r
import numpy as np
from Alteration import binaryconv as bn

characters, dic1 , dic2 = r.dictGen()

#converting sting key into numeric matrix
def keyFormat(key):
    klen = len(key) #string key
    keymLen = int(math.sqrt(klen)) #key matrix row length

    k = []
    for i in range(klen):
        k.append(dic1[key[i]])

    key = []
    for i in range(0,klen,keymLen):
        key.append(k[i:i+keymLen])

    return key

def encryption(key, text, tfname):
    key = keyFormat(key)

    #list to matrix
    K = np.matrix(key)

    padded_text = r.msgpadding(text,K,0)
    encrypted_message = h.encrypt(padded_text, K)

    padded_message = r.msgpadding(encrypted_message,K,1)
    binary_message = bn.str2bits(padded_message)
    buzz = bn.bazi(binary_message,key)
    buzz = bn.baziPRO(buzz,key)
    tfname += "enc.txt"

    #saving into file
    with open(tfname, 'w') as file:
        file.write(buzz)


def decryption(key,text,tfname):
    key = keyFormat(key)

    #list to matrix convertion
    K = np.matrix(key)
    #finding key matrix inversse
    Kinv = r.matrix_mod_inv(K, 89)
    Kinv = np.matrix(Kinv)

    buzz = bn.baziPRO(text,key)
    buzz = bn.bazi(buzz,key)
    string_message = bn.bit2str(buzz)
    unpadded_message =  r.msgpaddremoving(string_message,K,1)
    decrypted_message = h.decrypt(unpadded_message, Kinv)
    message = r.msgpaddremoving(decrypted_message,K,0)
    tfname += "dec.txt"

    #saving into file
    with open(tfname, 'w') as file:
        file.write(message)
