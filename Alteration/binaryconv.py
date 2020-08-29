from Alteration import bazinga as buzz
#import bazinga as buzz
from ast import literal_eval

#string to bit convertion
def str2bits(s):
	return "".join([bin(ord(x))[2:].zfill(8) for x in s])

#accessing bazinga
def bazi(s,k):
	return buzz.bazingaAlgo(s,k)

def baziPRO(s,k):
	return buzz.bazingaAlgoPRO(s,k)

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

#for hexa convertion
def bit2hexa(b=""):
	b_num = []
	s = ""
	flag = 0
	result = ""
	for i in range(len(b)):
		if b[i] == '0' and flag == i:
			s += b[i]
			flag += 1
			continue

		b_num.append(b[i])

	value = 0

	for i in range(len(b_num)):
	   digit = b_num.pop()
	   if digit == '1':
			  value = value + pow(2, i)
	result = str(hex(value))
	result += " "+s
	return result

#for hrxa to binary convertion
def hexa2bit(h=""):
	s = ""
	for i in range(len(h)-1,0,-1):
		if h[i] != '0':
			break
		s += '0'
	h = h[0:i]

	res = int(literal_eval(h))
	res = str(bin(res).replace("0b",""))
	res = s + res
	return res
