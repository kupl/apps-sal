import re

def increment_string(s):
    n = ''.join(re.findall(r'\d*$', s))
    l = len(s) - len(n)
    n = '0' if n == '' else n
    
    return s[:l] + '%0*d' % (len(n), int(n) + 1)
