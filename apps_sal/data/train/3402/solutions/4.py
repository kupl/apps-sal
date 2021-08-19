def calculate(a, o, b):
    if o == "+":
        return a + b
    if o == "-":
        return a - b
    if o == "*":
        return a * b
    if o == "/" and b != 0:
        return a / b


# one-liner
#    return [a+b, a-b, a*b, a/b if b else None, None]["+-*/".find(o)]
