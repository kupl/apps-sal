import re

ADDSUB, MULDIV = '+-', '*$'

def calculate(expression):
    return "400: Bad request" if re.search(r'[^+*$\d.-]', expression) else parseAndEval(expression, ADDSUB)

def parseAndEval(expression, ops):
    v = 0
    for op,part in re.findall(r'([{0}])?([^{0}]+)'.format(ops), expression):
        if not op:    v  = float(part) if ops == MULDIV else parseAndEval(part, MULDIV)
        elif op=='*': v *= float(part)
        elif op=='$': v /= float(part)
        elif op=='+': v += parseAndEval(part, MULDIV)
        elif op=='-': v -= parseAndEval(part, MULDIV)
    return v
