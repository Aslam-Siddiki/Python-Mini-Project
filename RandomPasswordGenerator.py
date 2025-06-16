import random
import string

len = int(input("Enter length of password: "))
pass_len = len
charValue = string.ascii_letters + string.digits + string.punctuation

Password = ""
for i in range(pass_len):
    Password += random.choice(charValue)
    
print(f"Your Password is: {Password}")    
