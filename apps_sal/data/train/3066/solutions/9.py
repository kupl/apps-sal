import re

class Expr:
    def __init__(self, terms):
        self.terms = terms
    def __add__(self, other):
        return Expr(self.terms + other.terms)
    def __sub__(self, other):
        return self + -other
    def __neg__(self):
        return Expr([(sign ^ 1, var) for sign, var in self.terms])
    def __str__(self):
        return ''.join('+-'[sign] + var for sign, var in self.terms).strip('+')

def solve(s):
    return str(eval(re.sub('(\w+)', r'Expr([(0, "\1")])', s)))

