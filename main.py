def add(num1, num2): 
    sum=(num1 + num2)
    return sum

def subtract(num1, num2):
    difference=(num1 - num2)
    return difference

def multiply(num1, num2):
    product=(num1 * num2)
    return product

def divide(num1, num2):
    if num2==0:
        print("num2 cannot be 0")
        return
    quotient=(num1 / num2)
    return quotient

num1 = input("Enter 1st value : ")
num2 = input("Enter 2nd value : ")

num1 = int(num1)
num2 = int(num2)

operation = input("Enter operation (add,subtract,multiply,divide): ")
if operation == "add":
    print(add(num1,num2))
elif operation == "subtract":
    print(subtract(num1,num2))
elif operation == "multiply":
    print(multiply(num1,num2))
elif operation == "divide":
    print(divide(num1,num2))

# add coment