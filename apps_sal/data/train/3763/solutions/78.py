def calculator(x,y,op):
    ops = {'+': 'x + y',
           '-': 'x - y',
           '/': 'x / y',
           '*': 'x * y'
          }
    if str(x).isnumeric() and str(y).isnumeric() and op in ops.keys():
        return eval(ops[op])
    else:
        return 'unknown value'
