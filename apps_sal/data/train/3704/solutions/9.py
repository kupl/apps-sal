class Exp:
    def __init__(self, s):
        self.a = 1 
        self.p = 0
        if s[-1] == 'x':
            self.p = 1
            s = s[:-1]
        if 0 < len(s):
            self.a *= int (s)
    
    def __add__(self, other):
        if self.p == other.p:
            self.a += other.a
            return self
        else:
            return Equ([self, other])
    
    def __sub__(self, other):
        if self.p == other.p:
            self.a -= other.a
            return self
        else:
            return Equ([self, Exp("-1") * other])

    def __mul__(self, other):
        self.p += other.p
        self.a *= other.a
        return self
    
    def __div__(self, other):
        self.p -= other.p
        self.a /= other.a
        return self
        
    def __str__(self):
        s = ""
        if self.a != 0:
            s += str(self.a)
        if (self.p) == 1:
            s += 'x'
        if s == "":
            s += '0'
        return s
        

class Equ:
    def __init__(self, exp):
        self.exp = dict()
        for e in exp:
            if e.p not in self.exp:
                self.exp[e.p] = e
            else:
                self.exp[e.p] += e
        
    def __add__(self, other):
        if type(other) == Exp:
            other = Equ([other])
        for p in other.exp:
            if p in self.exp:
                self.exp[p] += other.exp[p]
            else:
                self.exp[p] = other.exp[p]
        return self

    def __sub__(self, other):
        if type(other) == Exp:
            other = Equ([other])
        for p in other.exp:
            if p in self.exp:
                self.exp[p] -= other.exp[p]
            else:
                self.exp[p] = Exp("-1") * other.exp[p]
        return self
                
    def __mul__(self, other):
        if type(other) == Exp:
            other = Equ([other])
        res = None
        for p1 in other.exp:
            temp_res = []
            for p2 in self.exp:
                temp_res.append(self.exp[p2] * other.exp[p1])
            if res is None:
                res = Equ(temp_res)
            else:
                res += Equ(temp_res)
        return self

    def __div__(self, other):
        if type(other) == Exp:
            other = Equ([other])
        res = None
        for p1 in other.exp:
            temp_res = []
            for p2 in self.exp:
                temp_res.append(self.exp[p2] / other.exp[p1])
            if res is None:
                res = Equ(temp_res)
            else:
                res += Equ(temp_res)
        return self
        
    def __str__(self):
        s = ""
        for p in self.exp:
            s += ' (' + str(self.exp[p]) + ') +'
        return s[:-1]

    def get_power(self, p):
        return self.exp[p] if p in self.exp else Exp("0") if p==0 else Exp("0x")


def build1(s):
    s = s.replace(' ', '')
    stack = []
    s += '!'
    if s[0] == '-':
        s = '0' + s
    j = 0
    for i in range(len(s)):
        if s[i] in ['+','-','*','/','(',')','!']:
            if j < i:
                stack.append(s[j:i])
            stack.append(s[i])
            j = i+1
    stack.remove('!')
    for i, x in enumerate(stack):
        if x not in ['+','-','*','/','(',')','!']:
            stack[i] = Exp(x)
    return stack
    
def build2(s):
    while ')' in s: 
        end = s.index(')')
        start = end
        while s[start] != '(':
            start -= 1
        s = s[:start] + [build2(s[start+1:end])] + s[end+1:]
    op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y,
          '/': lambda x, y: x.__div__(y) }
    i = 2
    for order in [0, 1]:
        i = 2
        while i < len(s):
            if (order == 0 and s[i-1] in ['*', '/']) \
            or (order == 1 and s[i-1] in ['+', '-']):
                s[i-2] = op[s[i-1]](s[i-2], s[i])
                s.pop(i)
                s.pop(i-1)
            else:
                i += 2
    return s[0]
        
def build(s):
    stack = build1(s)
    equ = build2(stack)
    if type(equ) == Exp:
        equ = Equ([equ])
    return equ
  

def solve_for_x(equation):
    l, r = equation.split(" = ")
    l, r = build(l), build(r)
    l, r = l.get_power(1) - r.get_power(1), r.get_power(0) - l.get_power(0)
    return r.a / l.a
