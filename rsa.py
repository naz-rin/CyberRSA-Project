quit = 1
message = input("What is the message?: ")
encrypted_message = ""
e = input("What is the e value?: ")
n = input("What is the n value?: ")
d = input("What is the d value?: ")

while quit != 2:
	print("Encrypt, Decrypt, or Exit?")
	answer=input("----->")
	if answer == ("3") or ('3') or ('3') or ('3'):
		quit += 1
		print ("Exiting...")
		break
	elif answer == ("Encrypt") or ('Encrypt') or ('encrypt') or ("encrypt"):
		encryption()
	elif answer == ("Decrypt") or ('Decrypt') or ('decrypt') or ("decrypt"):
		decryption()

def encryption():
	for c in message:
		numerize = ord(c)
		encrypt = pow(numerize, e, n)
		denumerize = chr(encrypt)
		encrypted_message += denumerize
		print (encrypted_message)
		
def decryption():
  for u in encrypted_message:
  	numerize = ord(u)
  	decrypt = pow(numerize, d, n)
  print (decrypt)