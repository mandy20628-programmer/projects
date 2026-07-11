# password generator
import random
import string
a=input("lowercase or uppercase or numbers? (l/u/n) ") 
b=input("symbols")
try:
    c=int(input("unique characters?  "))
except ValueError:
    print("Please enter a valid integer for unique characters.")
d=input("similar characters?  ")
e=input("passwords: ")
try:
    f=int(input("length: "))
except ValueError:
    print("Please enter a valid integer for the length.")

if a == "l":
    alphabet = string.ascii_lowercase
elif a == "u":
    alphabet = string.ascii_uppercase
elif a == "n":
    alphabet = string.digits

symbols = b
final = alphabet + symbols

def se ():
    w= False
    x= False    
    while True:
        passwords = random.choices(final, k=f)
        for i in passwords:
            if i in alphabet:
                w=True
            if i in symbols:
                x=True
        if x and w == True:
                break

    print("".join(passwords))
se()

