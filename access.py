import main as h
from KeyGenerator import randomgen as re
from Alteration import binaryconv as bn
from Alteration import bazinga as buzz

def process(fn):
	fn += ".bin"
	try:
		with open(fn, 'r+') as file:
			text = file.read()
			text = bn.kbit2str(text)


		return text
	except IOError:
		print("file not!found")
		return -1

def display(fn,y):
	fn += ".txt"
	try:
		with open(fn, 'r') as file:
			text = file.read()
		if y == "e":
			print("\n" + bn.kbit2str(text))
		elif y == "d":
			print("\n" + text)
	except IOError:
		print("file not!found")


while True:
	print ("""
	1. Encryption
	2. Decryption
	3. Display encription file
	4. Display decryption file
	5. Display plain text file
	6. Exit
	""")

	ch = input("Enter your choice : ")
	if ch == "1":
		ans=input("\nDo you want to create key :(y,n) ")
		if ans.lower() == 'y':
			kfname = input("Enter Key filename: ")
			kfname += ".bin"

			key = re.keyGen()
			print("Key Generated!")
			k = bn.kstr2bits(key)


			with open(kfname, 'w') as file:
				file.write(k)

		elif ans.lower() == 'n':
			kfile = input("\nEnter Key filename: ")

			key = process(kfile)
			if key == -1:
				continue

		else:
			print("Wrong choice!")
			continue
		textfile = input("\nEnter text filename to be encrypted: ")
		textfile += ".txt"
		try:
			with open(textfile, 'r+') as file:
				text = file.read()
				text = text.rstrip()
		except IOError:
			print("file not found")
			continue
		h.encryption(key,text,textfile[:-4])
		print("Encryption completed!")
		print("File is saved as "+textfile[:-4]+"enc.txt" )

	elif ch == "2":
		kfile = input("\nEnter Key filename: ")
		key = process(kfile)

		if key == -1:
			continue

		textfile = input("\nEnter text filename to be decrypted: ")
		textfile += ".txt"

		try:
			with open(textfile, 'r+') as file:
				text = file.read()
		except IOError:
			print("file not found")
			continue

		h.decryption(key,text,textfile[:-4])
		print("Decryption completed!")
		print("File is saved as "+textfile[:-4]+"dec.txt" )
	elif ch == "3":
		fn = input("Enter file name: ")
		display(fn,"e")
	elif ch == "4":
		fn = input("Enter file name: ")
		display(fn,"d")
	elif ch == "5":
		fn = input("Enter file name: ")
		display(fn,"d")
	elif ch == "6":
		break
	else:
		print("Wrong choice!")
