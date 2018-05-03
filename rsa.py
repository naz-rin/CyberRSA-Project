terminate = 0
while terminate != 1:
	print("Encrypt, Decrypt, or Terminate?")
	answer=input("----->")
	if answer == "Terminate":
		terminate += 1
		print ("Exiting...")
	elif answer == "Encrypt":
		encryption(e,n)
  elif answer == "Decrypt":
    decryption(d,n)
    
def encryption(e,n):
	print ("what is the message?")
  e = input("What is the e value?")
  n = input("What is the n value?")
  message = input="message:"
  encrypted_message=""
  for c in message:
		numerize = ord(c)
		encrypt = pow(numerize, e, n)
		denumerize = chr(encrypt)
		encrypted_message += denumerize
		print (encrypted_message)
		
def decryption(d,n):
  d = input("What is the d vaule?")
  for u in encrypted_message:
  	numerize = ord(u)
  	decrypt = pow(numerize, d, n)
  print (decrypt)