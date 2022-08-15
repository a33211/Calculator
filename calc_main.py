import sys
import chime
from termcolor import colored, cprint

tempSumm = 0


# function call
# def decorator(func):
#     def wrap(*args):
#         number1 = cprint(x, 'white', attrs='bold')
#         number2 = cprint(x, 'green', attrs='bold')
#         return number1, number2
#     return wrap

def soundDec(func):
    def wrap(*args):
        chime.theme("zelda")
        chime.success()
    return wrap()


def func_add(number1, number2):
    result = number1 + number2
    chime.theme("zelda")
    chime.success()
    return result

#@soundDec
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
    ending = colored("Bye bye", 'red', attrs=['reverse', 'blink'])
    print(ending)
    chime.error()
    quit()


# @decorator
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
            answer = cprint(f"Answer is {func(number1, number2)} \n", 'cyan', attrs=['bold'], file=sys.stderr)
            print(f"Answer is {func(number1, number2)} \n")
            # tempSumm = result


parser = {"+": func_add,
          "-": func_min,
          "*": func_mult,
          "/": func_div,
          "q": func_exit}

while True:
    execute()

# Fix UnboundLocalError
# Fix decorator

