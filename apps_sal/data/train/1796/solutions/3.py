class Stack(object):

    def __init__(self):
        self.stack = []

    def getStack(self):
        return ''.join(self.stack)

    def peek(self):
        try:
            return self.stack[0]
        except IndexError as e:
            raise ValueError(e)

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        try:
            return self.stack.pop(0)
        except IndexError as e:
            raise ValueError(e)

    def push(self, v):
        self.stack.insert(0, v)


class Ifix2PfixConverter:
    __EXP_OP = '^'
    __MUL_OP = '*'
    __DIV_OP = '/'
    __ADD_OP = '+'
    __SUB_OP = '-'
    __L_PAREN = '('
    __R_PAREN = ')'
    __precidenceTable = {__EXP_OP: 4, __MUL_OP: 3, __DIV_OP: 3, __ADD_OP: 2, __SUB_OP: 2}
    __associativityTable = {__EXP_OP: 'right', __MUL_OP: 'left', __DIV_OP: 'left', __ADD_OP: 'left', __SUB_OP: 'left'}

    def __init__(self, eqn):
        self.infixEqn = eqn
        self.postfixEqn = []
        self.stack = Stack()
        self.convertToPostfix()

    def isLeftAssociative(self, k):
        return 'left' == self.__associativityTable[k]

    def getPostfixEquation(self):
        return ''.join(self.postfixEqn)

    def isOperator(self, k):
        return k in self.__precidenceTable

    def precidence(self, k):
        return self.__precidenceTable[k]

    def isOperand(self, k):
        return k.isalnum()

    def isLeftParen(self, k):
        return k == self.__L_PAREN

    def isRightParen(self, k):
        return k == self.__R_PAREN

    def convertToPostfix(self):
        for c in self.infixEqn:
            if self.isOperand(c):
                self.postfixEqn.append(c)
            elif self.isLeftParen(c):
                self.stack.push(c)
            elif self.isRightParen(c):
                while not self.stack.isEmpty() and (not self.isLeftParen(self.stack.peek())):
                    self.postfixEqn.append(self.stack.pop())
                self.stack.pop()
            elif self.isOperator(c):
                while not self.stack.isEmpty() and self.isOperator(self.stack.peek()) and (self.precidence(self.stack.peek()) > self.precidence(c) or (self.precidence(self.stack.peek()) == self.precidence(c) and self.isLeftAssociative(c))):
                    self.postfixEqn.append(self.stack.pop())
                self.stack.push(c)
            else:
                raise ValueError('Uknown Character [', c, '] Encountered')
        while not self.stack.isEmpty():
            self.postfixEqn.append(self.stack.pop())


def to_postfix(infix):
    converter = Ifix2PfixConverter(infix)
    return converter.getPostfixEquation()
