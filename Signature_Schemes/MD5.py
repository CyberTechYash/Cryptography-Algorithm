import hashlib

# initializing string
str2hash = input("Enter the plain text: ")

# encoding
# then sending to md5()

result = hashlib.md5(str2hash.encode())

# printing the equivalent hexadecimal value.

print("The hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())

