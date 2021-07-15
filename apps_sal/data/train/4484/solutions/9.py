from operator import add, sub, mul, truediv as div

operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculate(n1, op, n2):
    return operators.get(op, lambda m, n: None)(n1, n2) if f"{op}{n2}" != "/0" else None
