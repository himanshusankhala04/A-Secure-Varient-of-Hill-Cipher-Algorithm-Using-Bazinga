import main as h
from KeyGenerator import randomgen as re
from Alteration import binaryconv as bn
from Alteration import bazinga as buzz
import time




def display(fn,y):
	fn += ".txt"
	try:
		with open(fn, 'r') as file:
			text = file.read()
		if y == "e":
			#print("\n" + bn.kbit2str(text))
			print("\n" + text)
		elif y == "d":
			print("\n" + text)
	except IOError:
		print("file not!found")


while True:
	print ("""
	1. Encryption
	2. Decryption
	3. Key generation
	4. Display encription file
	5. Display decryption file
	6. Display plain text file
	7. Display key from key file
	8. Exit
	""")

	ch = input("Enter your choice : ")
	if ch == "1":
		ans=input("\nDo you want to create key :(y,n) ")
		if ans.lower() == 'y':
			kfname = input("Enter Key filename: ")
			kfname += ".txt"

			key = re.keyGen()
			print("Key Generated!")

			with open(kfname, 'w') as file:
				file.write(key)

		elif ans.lower() == 'n':
			kfile = input("\nEnter Key filename: ")

			kfile += ".txt"
			try:
				with open(kfile, 'r') as file:
					key = file.read()

			except IOError:
				print("file not!found")
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
		kfile += ".txt"
		try:
			with open(kfile, 'r') as file:
				key = file.read()

			textfile = input("\nEnter text filename to be decrypted: ")
			textfile += ".txt"

			with open(textfile, 'r+') as file:
				text = file.read()
		except IOError:
			print("file not found")
			continue

		h.decryption(key,text,textfile[:-4])
		print("Decryption completed!")
		print("File is saved as "+textfile[:-4]+"dec.txt" )
	elif ch == "3":
		kfname = input("Enter Key filename: ")
		kfname += ".txt"

		key = re.keyGen()
		print("Key Generated!")

		with open(kfname, 'w') as file:
			file.write(key)

	elif ch == "4":
		fn = input("Enter file name: ")
		display(fn,"e")

	elif ch == "5":
		fn = input("Enter file name: ")
		display(fn,"d")

	elif ch == "6":
		fn = input("Enter file name: ")
		display(fn,"d")

	elif ch == "7":
		fn = input("Enter key file name: ")
		x = process(fn)
		if x == -1:
			print('file not found')
			continue
		print(x)

	elif ch == "8":
		break
	else:
		print("Wrong choice!")
