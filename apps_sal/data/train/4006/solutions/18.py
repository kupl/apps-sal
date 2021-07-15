import operator
def basic_op(op, value1, value2):
    oper={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    return oper[op](value1,value2)
