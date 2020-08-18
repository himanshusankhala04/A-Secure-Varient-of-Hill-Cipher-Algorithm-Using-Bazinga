import secrets
import numpy as np
from egcd import egcd


secretsGenerator = secrets.SystemRandom()
characters =" abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&()_-+={[}],\:'/*.?"+'"'

l1 = [characters[i:i+1] for i in range(0,len(characters))]


dic1 = dict(zip(characters, range(len(characters))))
dic2 = dict(zip(range(len(characters)), characters))


def matrix_mod_inv(matrix, modulus):
 
    det = int(np.round(np.linalg.det(matrix)))  # Step 1)
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Step 3)

    return matrix_modulus_inv



def dictGen():

    return characters,dic1,dic2

def keyGen():

    klen = secretsGenerator.choice(range(4,7)) #select  random key length between[4,5,6]
    flag = True #key checker

    #selecting mod
    if klen == 6:
        md = 30
    elif klen == 5:
        md = 69
    else:
        md = 89

    #random key generator
    while flag:
        k = []
        for i in range(0,klen):
            k1 = []
            for j in range(0,klen):
                k1.append(secretsGenerator.choice(range(md)))
            k.append(k1)

        det1 = int(np.round(np.linalg.det(k)))

        #1st condition det should not equal to 0
        if det1 != 0:
            flag = False

        inv1 = matrix_mod_inv(np.matrix(k), len(characters))
        inv1 = inv1.tolist()
        count = 0
        sum1 = 0

        #2nd condition key matrix inverse should not contain all 0 values
        for i in range(0,klen):
            for j in range(0,klen):
                sum1 += inv1[i][j]
                if inv1[i][j] == 0:
                    count += 1

        if count == klen**2:
            flag = True

    key = []
    #key in text convertor
    for i in range(0,klen):
        for j in range(0,klen):
            key.append(dic2[k[i][j]])

    return "".join(key)



def msgpadding(msg,k):

    paddpattern = []
    #padding pattern selector
    for i in range(len(k[0])):
        paddpattern.append(min(k[i]))

    c = 0
    ms = 0 #message pointer

    #padding into message
    while ms+(paddpattern[c]%10) < len(msg):
        padd = ""

        if ms+(paddpattern[c]%10) == 0:
            for i in range(dic1[msg[ms+(paddpattern[c]%10)]] % len(k[0])):
                padd += secretsGenerator.choice(l1) #creating padding strng randomly

            msg = msg[0] + padd + msg[1:]
            ms += 1 + len(padd) #incrementing pointer

        else:
            for i in range(dic1[msg[ms+(paddpattern[c]%10)-1]] % len(k[0])):
                padd += secretsGenerator.choice(l1) #creating padding strng randomly

            msg = msg[0:ms+(paddpattern[c]%10)] + padd + msg[ms+(paddpattern[c]%10):]
            ms += (paddpattern[c]%10) + len(padd) #incrementing pointer
        c += 1
        if c == len(paddpattern):
            c = 0

    return msg

def msgpaddremoving(paddmsg,k):
    paddpattern = []
    #padding pattern selector
    for i in range(len(k[0])):
        paddpattern.append(min(k[i]))

    c = 0
    ms = 0 #padded message pointer
    msg = ""
    #padding removing
    while ms+(paddpattern[c]%10) < len(paddmsg) :

        if ms+(paddpattern[c]%10) == 0:
            val = dic1[paddmsg[0]] % len(k[0])
            msg += paddmsg[0]
            ms += val +1 #incrementing pointer
        else:
            val = dic1[paddmsg[(ms+(paddpattern[c]%10))-1]] % len(k[0])
            msg += paddmsg[ms:ms+(paddpattern[c]%10)]
            ms += (paddpattern[c]%10) + val #incrementing pointer

        c += 1
        if c == len(paddpattern):
            c = 0

    if ms <= len(paddmsg):
        msg += paddmsg[ms:]

    return msg
