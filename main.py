# optional section %, sqrt

class InitialCommand:
    def __init__(self, operand_1, operand_2, operator, result=None):
        self.result = result
        self.operand_1 = operand_1
        self.operand_2 = operand_2
        self.operator = operator

    @property
    def operand_1(self):
        return self._operand_1

    @operand_1.setter
    def operand_1(self, operand_1):
        try:
            float(operand_1)
            self._operand_1 = operand_1
            print(f'{operand_1} is a number')
        except ValueError:
            print('Please enter value')

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, operator) -> str:
        try:
            operator in commands
            self._operator = operator
        except ValueError:
            print('Please pick mathematical operation')

    @property
    def operand_2(self):
        return self._operand_2

    @operand_2.setter
    def operand_2(self, operand_2):
        try:
            float(operand_2)
            self._operand_1 = operand_2
            print(f'{operand_2} is a number')
        except ValueError:
            print('Please enter value')

    def init_():
        operand_1 = input('>>>')
        try:
            int(operand_1)
        except ValueError:
            print("Please enter number to strat calculation")
        operator = input('Please enter operation')
        try:
            operator in commands
        except ValueError:
            print("Please enter operation")
        operand_2 = input('>>>>')
        try:
            int(operand_2)
        except ValueError:
            print("Please enter number to strat calculation")

        match operator:
            case '+':
                result = Add.add()
                print(result)
            case '-':
                result = Subtract.subtract()
                print(result)
            case '*':
                result = Multiply.multiply()
                print(result)
            case '/':
                result = Divide.divide()
                print(result)

            # Function section


class Add(InitialCommand):
    def add(self, operand_1, operand_2) -> float:
        self.result = operand_1 + operand_2
        return self.result


class Subtract(InitialCommand):
    def subtract(self, operand_1, operator, operand_2, result) -> float:
        self.result = operand_1 - operand_2
        return self.result


class Multiply(InitialCommand):
    def multiply(self, operand_1, operator, operand_2, result) -> float:
        self.result = operand_1 * operand_2
        return self.result


class Divide(InitialCommand):
    def divide(self, operand_1, operator, operand_2, result) -> float:
        self.result = operand_1 / operand_2
        return self.result


commands = ['+', '-', '*', '/']

if __name__ == '__main__':
    run = InitialCommand.init_()
