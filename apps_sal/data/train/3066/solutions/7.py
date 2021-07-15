import re
from functools import reduce
def solve(s):
    sign, stack = {('+', '-'): '-', ('-', '+'): '-', ('+', '+'): '+', ('-', '-'): '+'}, []
    for i in s:
        if i != ')' : stack.append(i)
        else:
            t = len(stack) - stack[::-1].index('(') - 1
            stack.pop(t)
            ini = stack[t - 1]
            if ini in '+-' : stack[t:] = list(re.sub(r'(?<=\w)([-+])(?=\w)', lambda x: sign[(ini, x.group(1))], "".join(stack[t:])))
        stack = list(re.sub(r'([-+]+)', lambda g: reduce(lambda x, y: sign[(x, y)], list(g.group())), "".join(stack)))
    return "".join(stack).lstrip('+')
