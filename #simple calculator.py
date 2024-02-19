#simple calculator
x = 1
y = 2

z = x + y
print(z)

# this will contatenate the answer
x = input("What's x ?")
y = input("Whats y ?")

z = x + y
print(z)

# general purpose calculator
#change the operator on line 20 to (-, *, /, %)
x = input("What's x ?")
y = input("Whats y ?")

z = int(x) + int(y)
print(z)

# make it neater 
# using nesting technique
x = int(input("What's x ?"))
y = int(input("Whats y ?"))

print(x + y)


# float (decimal calculator)
x = float(input("Whats x? "))
y = float(input("Whats y? "))

print (x + y)

#round the nearest number
x = float(input("Whats x? "))
y = float(input("Whats y? "))

z = round(x + y)
print (z)


# using def function and return to multiply power of
def main():
    x = int(input("What's x? "))
    print("x squared is", square (x))

def square(n):
    return n * n
    
    main()


# This is a multi-purpose calculator
def calculator():
    operation=input('''
please type in the math operation you would like to use
                    +for addition
                    -for minus
                    *for multiplication
                    /for division
                    ''')
    x=int(input("What's x? "))
    y=int(input("What's y? "))
if operation == '+':
    print('{} + {} = '.format(x , y))
    print(x + y)
elif operation == '_':
    print('{} - {}'. format( x , y ))

# using define to create a calculator
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

# I managed to sort out if the user output is not an integar
    if type(number_1) == 'int' and type(number_2) == 'int' and operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

# Call calculate() outside of the function
calculate()

# Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()

#calculating 3 different numbers
x = int(input("What's x"))
y = int(input("What's y"))
z = int(input("Whats z"))

print(+(x, y), z)

#creating a multi-function calculator
x = int(input("\What's x? "))
operator = input("Please choose an input (+,*,-,/): ")
y=int(input("What's y? "))
operator = input("Please choose an input (*,/,+,-): ")

if operator == '+':
    print(x + y)
