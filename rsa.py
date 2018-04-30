quit = 1
message = ""
encrypted_message = ""

while quit != 2:
	print("Encrypt, Decrypt, or Exit?")
	answer=input("----->")
	if answer == ("3") or ('3') or ('3') or ('3'):
		quit += 1
		print ("Exiting...")
		break
	elif answer == ("Encrypt") or ('Encrypt') or ('encrypt') or ("encrypt"):
		encrypt()
	elif answer == ("Decrypt") or ('Decrypt') or ('decrypt') or ("decrypt"):
		decrypt()

def encrypt():
	for c in message:
		numerize = ord(c)
		encrypt = pow(numerize, e, n)
		denumerize = unichr(encrypt)
		encrypted_message += denumerize
		print (encrypted_message)