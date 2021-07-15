import operator as opr
def arithmetic(a, b, operator):
    operations = {
        "add":opr.add,
        "subtract":opr.sub,
        "multiply":opr.mul,
        "divide":opr.truediv
        }
    return operations[operator](a,b)

