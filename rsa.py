terminate = 0


def encryption(e,n):
	encrypted_message = ""
	message = input("Input Message: ")
	for x in message:
		numerize = ord(x)
		encrypt = pow(numerize, e, n)
		denumerize = chr(encrypt)
		encrypted_message += denumerize
	print(encrypted_message)
	print("")
	


def decryption(d,n):
	decrypted_message = ""
	encryptedmessage = input("Input encrypted message: ")
	for t in encryptedmessage:
		numerize = ord(t)
		decrypt = pow(numerize, d, n)
		denumerize = chr(decrypt)
		decrypted_message += denumerize
	print(decrypted_message)
	print("")
	
while terminate != 1:
	print("What would you like to do?")
	print("---------------Encrypt---------------")
	print("---------------Decrypt---------------")
	print("---------------Exit---------------")
	choice = input("---------------> ")
	if choice == "Encrypt":
		e = int(input("Enter your 'e' variable: "))
		n = int(input("Enter your 'n' variable: "))
		encryption(e,n)
	if choice == "Decrypt":
		d = int(input("Enter your 'd' variable: "))
		n = int(input("Enter your 'n' variable: "))
		decryption(d,n)
	if choice == 'Exit':
			break
