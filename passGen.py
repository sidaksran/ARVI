import random
import string
import re

# Random password length generated (Between 11-23 characters)
lengthChoices = 11,12,13,14,15,16,17,18,19,20,21,22,23
length = random.choice(lengthChoices)

# Generation of password
charChoices = string.ascii_lowercase + string.ascii_uppercase + string.digits + "-|@.,?/~#%^&*()}{\=*"
password = ''.join(random.choice(charChoices) for i in range(length))

# Validation of password
while True:
    if not re.search("[a-z]", password):
        valid = False
        break
    elif not re.search("[A-Z]", password):
        valid = False
        break
    elif not re.search("[0-9]", password):
        valid = False
        break
    elif not re.search("[-|@.,?/~#%^&*()}{\=*]", password):
        valid = False
        break
    else:
        valid = True
        break

# Print the password if valid or error
if valid == False:
    print("Invalid password generated. Try again!")
elif valid == True:
    print("Valid password generated:")
    print(password)