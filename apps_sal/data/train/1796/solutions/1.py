LEFT  = lambda a,b: a>=b
RIGHT = lambda a,b: a>b
PREC  = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4, '(': 1, ')': 1}

OP_ASSOCIATION = {'+': LEFT, '-': LEFT, '*': LEFT, '/': LEFT, '^': RIGHT}


def to_postfix (infix):
    stack, output = [], []
    for c in infix:
        prec = PREC.get(c)
        
        if prec is None: output.append(c)
        elif c == '(':   stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output.append( stack.pop() )
            stack.pop()
        else:
            while stack and OP_ASSOCIATION[c](PREC[stack[-1]], prec):
                output.append( stack.pop() )
            stack.append(c)
            
    return ''.join(output + stack[::-1])
