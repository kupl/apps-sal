import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  
    #'%' : operator.mod,
    #'^' : operator.xor,
}


def calculator(x,y,op):
    print((x, y, op))
    a = (type(x), type(y), type(op))
    if a[0] != int or a[1] != int:
        return "unknown value"
    print(a)
    try:
        q = ops[op](x,y)
        return q
    except:
        return "unknown value"

