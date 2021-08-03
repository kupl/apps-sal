import re


class Exp(object):
    def __init__(self, v='x'):
        self.exp = v

    def __str__(self): return self.exp
    def make(self, other, sign, r=1): return Exp('({}{}{})'.format(*[self.exp, sign, str(other)][::r]))
    def oparation(self, a, b, sign): return str(a + b if sign == '+' else a - b if sign == '-' else a * b if sign == '*' else a // b)

    def __call__(self, *args, sr=r'\((-?\d+)([+\-*/])(-?\d+)\)'):
        args = list(args)
        s = re.sub(r'x', lambda x: str(args.pop(0)), self.exp)
        k = re.search(sr, s)
        while k:
            a, sign, b = k.groups()
            s = s[:k.start()] + self.oparation(int(a), int(b), sign) + s[k.end():]
            k = re.search(sr, s)
        return int(s)


x = Exp()
for i, j in zip('add sub mul floordiv radd rsub rmul rfloordiv'.split(), ('+-*/' * 2)):
    setattr(Exp, f'__{i}__', lambda self, other, sign=j, r=[1, -1][i[0] == 'r']: self.make(other, sign, r))
