def Addition():    # Creating a function for Addition between numbers
    a = int(input("Enter any first value:- "))   # Input first number
    b = int(input("Enter any second value:- "))  # Input second number
    c = a + b
    print(f"Answer is {c}")
  

def Subtraction():     # Creating a function for Subtraction between numbers
    a = int(input("Enter any first value:- "))
    b = int(input("Enter any second value:- "))
    c = a - b
    print(f"Answer is {c}")
 

def Division():    # Creating a function for Division between numbers
    a = int(input("Enter any first value:- "))
    b = int(input("Enter any second value:- "))
    c = a/b
    print(f"Answer is {c}")


def Multiply():     # Creating a function for Multiplication between numbers
    a = int(input("Enter any first value:- "))
    b = int(input("Enter any second value:- "))
    c = a * b
    print(f"Answer is {c}")


while True: # created a loop for repeating funtion many times
    print("------------------------\n1. Add 'a'\n2. Sub 's'\n3. Div 'd'\n4. Mul 'm'\n5. 'q' for quit \n---------------------")

    i = input("Choose your operation that you want to perform: ")

    if i != 'q':

        if i == 'a':
            list = Addition()  # Calling funtion
            print(list)


        elif i == 's':
            list = Subtraction()  # Calling function
            print(list)


        elif i == 'd':
            list = Division()   # Calling funtion
            print(list)


        elif i == 'm':
            list = Multiply()   # Calling function
            print(list)

        else:
            print("Choose a valid option!") # when you give wrong input

    else:
        break
