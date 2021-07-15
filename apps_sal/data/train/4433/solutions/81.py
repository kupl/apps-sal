from functools import reduce
def logical_calc(array, op):
    if op=='XOR':
        op='^'
    return reduce(lambda a,b:eval(str(a)+' '+op.lower()+' '+str(b)),array)
