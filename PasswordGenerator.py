import string
import random

allowed = []
password = ""
cnt = 0

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
numbers = list(string.digits)
specialChars = '$ % ^ & * ( ) _ + = - ! ; : , . [ ] { }'.split()

random.shuffle(lower)
random.shuffle(upper)
random.shuffle(numbers)
random.shuffle(specialChars)

length = int(input("Enter Password Length: "))
lowerCase = input("LowerCase Allowed (y/n): ")
upperCase = input("UpperCase Allowed (y/n): ")
number = input("Number Allowed (y/n): ")
special = input("Special Character Allowed (y/n): ")

if lowerCase.lower() == 'y':
    allowed.append(lower)
    cnt += 1
    password += random.choice(lower)

if upperCase.lower() == 'y':
    allowed.append(upper)
    password += random.choice(upper)
    cnt += 1

if number.lower() == 'y':
    allowed.append(numbers)
    cnt += 1
    password += random.choice(numbers)

if special.lower() == 'y':
    allowed.append(specialChars)
    cnt += 1
    password += random.choice(specialChars)


if cnt == 0:
    print("At least one Y is required")
    exit()


def selectRandTypeInd():
    type = random.randint(0, len(allowed)-1)
    ind = random.randint(0, len(allowed[type])-1)
    return allowed[type][ind]


for _ in range(length-cnt):
    password += selectRandTypeInd()

password = list(password)
random.shuffle(password)
password = "".join(password[:length])

print("-"*20, "Password", "-"*20)
print(password)
