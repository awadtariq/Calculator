#creating a multi-function calculator
x = int(input("What's x? "))
operator = input("Please choose an input (+,*,-,/): ")
y=int(input("What's y? "))
operator = input("Please choose an input (*,/,+,-): ")
z=int(input("What's z? "))

if operator == '+':
    z = int(input("What's z? "))
    print(x + y)

elif operator == '-':
    z = int(input("What's z? "))
    print(x + y)
elif operator == '*':
    z = int(input("What's z? "))
    print(x*y)
elif operator == '/':
    z = int(input("Whats's z? "))
    print(x/y)

else:
    print("Calculation invalid. ")




