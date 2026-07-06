from random import randint
a=randint(1, 100)
while True:
        try:
            b=int(input("Enter a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
            if a==b:
                print("You guessed it!")
                print("The number was:", a) 
                break
            if a>b:
                        print("try a higher number!")
            else:
                        print("try a lower number!")
a=(input("want to play again? (y/n): "))
if a == "y":
    exec(open("03_project.py").read())  