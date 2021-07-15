class Calculator(object):

    operators = {'+': lambda x,y: x+ y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y }
    high_pre = ['*', '/']

    def __init__(self):
        self.operand = []
        self.operator = []

    def parse_string(self, string):
        index = 0
        while index < len(string):
            end = index + 1
            while end < len(string) and string[end] not in list(self.operators.keys()):
                end += 1
            try:
                self.operand.append(float(string[index:end]))
            except:
                return False
            if end < len(string):
                self.operator.append(string[end])
            index = end + 1
        return True

    def evaluate(self, string = ""):
        if string == "":
            string = "0"

        valid = self.parse_string(string)
        if not valid:
            return False

        while len(self.operand) != 1:
            operator_index = len(string)
            for op in self.high_pre:
                if op in self.operator:
                    operator_index = min(operator_index, self.operator.index(op))
            if operator_index == len(string):
                operator_index = 0
            x = self.operand[operator_index]
            y = self.operand[operator_index + 1]
            op = self.operator[operator_index]
            try:
                self.operand[operator_index] = self.operators[op](x, y)
            except:
                return False
            self.operand.pop(operator_index + 1)
            self.operator.pop(operator_index)

        return self.operand[0]
        

def calculate(input):
    if type(input) != str:
        return False
    return Calculator().evaluate(input)

