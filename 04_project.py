# CREATING A CALCULATOR
def calculator():
    a1=int(input("Enter the first number: "))
    b=input("Enter the operator (+, -, *, /): ")
    a2=int(input("Enter the second number: "))
    if b=="+":
        a=a1+a2
    elif b=="-":
        a=a1-a2
    elif b=="*":
        a=a1*a2    
    elif b=="/":
        a=a1/a2
    a3=input("enter the operator (+, -, *, /)to continue or = to" \
    " display the result: ")
    if a3=="=":
        print(f"the result is {a}")
    if a3=="+"or a3=="-"or a3=="*"or a3=="/":
        def calculator1(a3):
            nonlocal a
            a4=int(input("Enter the next number: "))
            if a3=="+":
                a=a+a4
            elif a3=="-":
                a=a-a4
            elif a3=="*":
                a=a*a4
            elif a3=="/":
                a=a/a4
            a5=input("enter the operator (+, -, *, /)to continue or = to" \
            " display the result: ")
            if a5=="=":
                print(f"the result is {a}")
            else:
                calculator1(a5)
        calculator1(a3)

        
            

calculator()
