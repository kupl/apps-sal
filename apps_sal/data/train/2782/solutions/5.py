def calc(expr):
    oplist=[]
    if expr=='': return 0
    for op in expr.split(' '):
        try:
            op=float(op)
            oplist.append(op)            
        except ValueError:
            op2=oplist.pop()
            op1=oplist.pop()
            oplist.append(eval(str(op1)+op+str(op2)))
    return oplist.pop()

