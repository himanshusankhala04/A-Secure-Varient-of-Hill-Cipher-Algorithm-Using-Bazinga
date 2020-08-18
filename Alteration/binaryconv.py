from Alteration import bazinga as buzz
#import bazinga as buzz

#string to bit convertion
def str2bits(s):
    return "".join([bin(ord(x))[2:].zfill(8) for x in s])

#accessing bazinga
def bazi(s,k):
    return buzz.bazingaAlgo(s,k)

#bit to string convertion
def bit2str(b):
    lis = []
    for i in range(0,len(b),8):
        lis.append(b[i:i+8])

    return "".join([chr(int(x,2)) for x in lis])

#for key
def kstr2bits(s=""):
    return buzz.kbazingaAlgo("".join([bin(ord(x))[2:].zfill(8) for x in s]))

#for key
def kbit2str(b=""):
    b = buzz.kbazingaAlgo(b)
    lis = []
    for i in range(0,len(b),8):
        lis.append(b[i:i+8])
    return "".join([chr(int(x,2)) for x in lis])
