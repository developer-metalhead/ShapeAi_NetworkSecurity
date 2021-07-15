import hashlib       # imports hashlib package to perform md5 encryption
hashing = input("Enter the string to md5 hash:- ")       # accepts the string from user to be hashed
hashed = hashlib.md5(hashing.encode())       # hashing the string 
print("Byte equivalent of hash is : ", hashed.digest())       # prints the Byte Equivalent of Hash
print("Hexadecimal equivalent of hash is : ", hashed.hexdigest())       # prints the Hexadecimal Equivalent of Hash
