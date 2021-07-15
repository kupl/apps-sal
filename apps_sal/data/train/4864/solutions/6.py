import re

def remove(s): return re.sub(r'(!*)([^! ]+)(!*)', repl, s)

def repl(m):
    s = '!' * min(map(len,(m[1],m[3])))
    return f'{s}{ m[2] }{s}'
