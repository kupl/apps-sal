ADD = "+"
SUB = "-"
MUL = "*"
DIV = "$"

OPS = {
    ADD: lambda x, y: x + y,
    SUB: lambda x, y: x - y,
    MUL: lambda x, y: x * y,
    DIV: lambda x, y: x / y,
}

DIGITS = "0123456789"

DECIMAL = "."

eMsg = "400: Bad request"


class RouteError(ValueError):
    pass

    '''
  IT IS NOT ALLOWED TO USE DOUBLE UNDERSCORE SEQUENSE IN THIS C_O_D_E,
  SO I HAVE TO WRITE MY CLASSES WITHOUT _ _init_ _
  def _ _init_ _(self, text):
    self.text=text
  '''


class Scaner:
    '''
    scans for tokens in input -
    arithmetic operations:    +   -   *   $
    and numbers:              1   2.  .3  4.5
    a decimal point is NOT a valid number, an exception is raised
    any other character also raises an exception
    '''

    '''
  IT IS NOT ALLOWED TO USE DOUBLE UNDERSCORE SEQUENSE IN THIS C_O_D_E,
  SO I HAVE TO WRITE MY CLASSES WITHOUT _ _init_ _
  def _ _init_ _(self, expression):
    self.exp=expression
    self.pos=0
    self.len=len(expression)
  '''

    def init(self, expression):
        self.exp = expression
        self.pos = 0
        self.len = len(expression)

    def get_digits(self):
        res = ""

        while self.pos < self.len:
            chr = self.exp[self.pos]
            if chr not in DIGITS:
                break
            res += chr
            self.pos += 1

        return res

    def get_number(self):
        num = self.get_digits()
        if self.pos >= self.len:
            return num

        if self.exp[self.pos] == DECIMAL:
            self.pos += 1
            num += DECIMAL + self.get_digits()
        if num == DECIMAL:
            raise RouteError("No digits in number.")
        return num

    def token(self):
        if self.pos >= self.len:
            return None

        chr = self.exp[self.pos]
        if chr in OPS:
            self.pos += 1
            return chr

        if chr in DIGITS or chr == DECIMAL:
            return self.get_number()

        self.pos += 1
        raise RouteError("Illegal character in expression.")


class Parser:
    '''
    parses tokens into reverse polish notation
    at first, all tokens are put into self.stk
    then they are rearranged and put into self.rpn
    1+2*3 -> 1 2 3 * +
    4-5+6 -> 4 5 - 6 +
    this class detects all errors in expression (except division by zero)
    so later we can evaluate rpn without error checking
    '''

    '''
  IT IS NOT ALLOWED TO USE DOUBLE UNDERSCORE SEQUENSE IN THIS C_O_D_E,
  SO I HAVE TO WRITE MY CLASSES WITHOUT _ _init_ _
  def _ _init_ _(self):
    self.stk=[]
    self.rpn=[]
  '''

    def init(self):
        self.stk = []
        self.rpn = []

    def pop(self):
        return self.stk.pop(0) if self.stk else None

    def token(self):
        return self.stk[0] if self.stk else None

    def generate_rpn(self):
        self.generate_subtraction()
        while self.token() == ADD:
            self.pop()
            self.generate_subtraction()
            self.generate_op(ADD)

        if self.stk:
            raise RouteError("Unexpected token " + self.token() + ".")

    def generate_subtraction(self):
        self.generate_multiplication()
        while self.token() == SUB:
            self.pop()
            self.generate_multiplication()
            self.generate_op(SUB)

    def generate_multiplication(self):
        self.generate_division()
        while self.token() == MUL:
            self.pop()
            self.generate_division()
            self.generate_op(MUL)

    def generate_division(self):
        if self.token() == None:
            raise RouteError("Missing operand 1.")
        self.generate_operand()
        while self.token() == DIV:
            self.pop()
            self.generate_operand()
            self.generate_op(DIV)

    def generate_operand(self):
        if not self.stk:
            raise RouteError("Missing operand 2.")
        if self.token() in OPS:
            raise RouteError("Unexpected operator " + self.token() + ".")
        tok = self.pop()
        self.rpn.append(float(tok) if DECIMAL in tok else int(tok))

    def generate_op(self, op):
        self.rpn.append(op)


def tryint(num):
    '''
    converts numbers like 2.0 to 2 without fractional part,
    like it is given in examples
    '''
    inum = int(num)
    return inum if num == inum else num


def Evaluate(rpn):
    '''
    evaluates rpn; error checking is not needed, because the data
    is sintacticaly correct after Parser
    (i. e., we will never get something like [1 2 + -] or [5 5])
    '''
    stk = []
    for t in rpn:
        if t in OPS:
            op0 = stk.pop()
            stk[-1] = OPS[t](stk[-1], op0)
        else:
            stk.append(t)

    return tryint(stk[0])


def calculate(expression):
    s = Scaner()
    s.init(expression)
    p = Parser()
    p.init()

    try:
        while True:
            t = s.token()
            if t:
                p.stk.append(t)
            else:
                p.generate_rpn()
                break

        res = Evaluate(p.rpn)

    except RouteError:
        res = eMsg
    except ZeroDivisionError:
        res = eMsg

    return res
