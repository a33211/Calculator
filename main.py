#optional section %, sqrt

class InitialCommand:
    def __init__(self, operand_1, operand_2, operator, result = None):
        self.result = result
        self.operand_1 = operand_1
        self.operand_2 = operand_2
        self.operator = operator

    @property
    def operand_1(self):
        return self._operand_1

    @operand_1.setter
    def operand_1(self, operand_1)->float:
        if type(operand_1) == float:
            self._operand_1 = operand_1

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, operator)->str:
        if operator is in : # !!!!!!!!!!I'd like to poit to parser->commands->keys
            self._operator = operator

    @property
    def operand_2(self):
        return self._operand_2

    @operand_2.setter
    def operand_2(self, operand_2)->float:
        if type(operand_2) == float:
            self._operand_2 = operand_2

#Function section
class Add(InitialCommand):
    def add(self)->float:
        if result == None:
            result = operand_1 + operand_2
        else:
          result += operand_1
        return result

class Subtract(InitialCommand):
    def subtract(self, operand_1, operator, operand_2, result)->float:
        pass

class Multiply(InitialCommand):
    def multiply(self, operand_1, operator, operand_2, result)->float:
        pass

class Divide(InitialCommand):
    def divide(self, operand_1, operator, operand_2, result)->float:
        pass

# PARSER
def parser(user_operator):
    commands = {'+': Add.add(),
                '-': Subtract.subtract(),
                '*': Multiply.multiply(),
                '/': Divide.divide()}
    # for user_operator in commands.keys():
    #     if user_operator == '':
    #         print('Operator is mandatory. Please enter valid operator')
    #         raise ValueError:
def init ():
    while True:
        operand_1 = float(input('Please enter first value for calculation\n'))
        operator = (input('Please enter operator calculation\n'))
        operand_2 = float(input('Please enter second value for calculation\n'))

        parser(user_input)
        run = Initial_command()





if __name__ == '__main__':
    init()

 # while true call
# input 1 - number
# input two - operand
# input 3 - number