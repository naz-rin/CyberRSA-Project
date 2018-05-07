terminate = 0
while terminate != 1:
	print("Encrypt, Decrypt, or Terminate?")
	answer=input("----->")
	if answer == "Terminate":
		terminate += 1
		print ("Exiting...")
	elif answer == "Encrypt":
		n=
		e=input("What is your ")
	elif answer == "Decrypt":
		print ("What is	")

def encryption(e,n):
	print ("what is the message?")
	message = input="Message:"
	encrypted_message=""
	for c in message:
		numerize = ord(c)
		encrypt = pow(numerize, e, n)
		denumerize = chr(encrypt)
		encrypted_message += denumerize
		print (encrypted_message)
		
def decryption(d,n):
  for u in encrypted_message:
  	numerize = ord(u)
  	decrypt = pow(numerize, d, n)
  print (decrypt)
