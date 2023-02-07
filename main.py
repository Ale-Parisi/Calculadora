#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
continuar = []
continuar = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
while continuar != "n":
    num3 = answer
    operation_symbol = input("Pick an operation: ")
    num4 = int(input("What's the next number?: "))
    answer = calculation_function(num3, num4)
    print(f"{num3} {operation_symbol} {num4} = {answer}")
    continuar = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")