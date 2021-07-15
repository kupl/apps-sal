from operator import add, sub, mul, truediv
D = {'+':add, '-':sub, '*':mul, '/':truediv}

def calculate(a, o, b):
    try: return D[o](a, b)
    except: pass
