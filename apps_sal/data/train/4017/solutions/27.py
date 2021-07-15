def add (a,b):      return a + b
def subt(a,b):      return add(a, -b)
def multiply(a,b):  return sum([max(a, b)] * min(a, b))
def divide(a,b):    return a // b
def mod(a,b):       return a - multiply(b, divide(a,b))
def exponent(a,b):  return multiply(a, exponent(a, b-1)) if b else 1
