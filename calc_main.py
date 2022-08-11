tempSumm = 0
# function call
def func_add(number1, number2):
    tempSumm = number1 + number2
    return tempSumm


def func_min(number1, number2):
    tempSumm = number1 - number2
    return tempSumm


def func_mult(number1, number2):
    tempSumm = number1 * number2
    return tempSumm


def func_div(number1, number2):
    tempSumm = number1 / number2
    return tempSumm


def execute(number1, number2, operator):
    for op, func in parser.items():
        if op == operator:
            tempSumm = func(number1, number2)
            print(f"Answer is {tempSumm}")


parser = {"+": func_add,
          "-": func_min,
          "*": func_mult,
          "/": func_div}

while True:
    number1 = input("1>>> \n")
    try:
        float(number1)
    except ValueError:
        print(" Please enter numerical value \n")
        number1 = input("1>>> \n")

    operator = input("please enter operation \n")
    if operator == "q":
        break
    validator = parser.get(operator)
    if not validator:
        print(" Please enter function to execute\n")
        operator = input("please enter operation \n")

    number2 = input("2>>> \n")

    try:
        float(number2)
    except ValueError:
        print(" Please enter numerical value \n")
        number1 = input("2>>> \n")

    execute(number1, number2, operator)
