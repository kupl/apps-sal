import operator


op = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}



def calculator(x,y,oper):
    print(x, y, op)
    try:
        return op[oper](x, y) if x > 0 and y > 0 else "unknown value"
    except:
        return "unknown value"
