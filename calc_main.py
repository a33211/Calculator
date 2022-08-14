tempSumm = 0
# function call


def func_add(number1, number2):
    result = number1 + number2
    return result


def func_min(number1, number2):
    result = number1 - number2
    return result


def func_mult(number1, number2):
    result = number1 * number2
    return result


def func_div(number1, number2):
    try:
        result = number1 / number2
    except ZeroDivisionError as error:
        print("Invalid equation \n")
        print(error)
    finally:
        return result

def func_exit(*args):
    print("Bye bye")
    quit()

def execute():
    try:
        number1 = float(input("1>>> \n"))
        number2 = float(input("2>>> \n"))
    except ValueError as error:
        print('You have entered not a number as an input\n')
        print(error)
        return
    operator = input("please enter operation \n")
    validator = parser.get(operator)
    if not validator:
        print(" Please enter function to execute\n")
        operator = input("please enter operation \n")

    for op, func in parser.items():
        if op == operator:
            print(f"Answer is {func(number1, number2)} \n")
            #tempSumm = result


parser = {"+": func_add,
          "-": func_min,
          "*": func_mult,
          "/": func_div,
          "q": func_exit}

while True:
    execute()

# Fix UnboundLocalError
# Add TempSum functional


