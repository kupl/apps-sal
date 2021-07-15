from itertools import cycle
def numeric_formatter(s,n="1234567890"):
    n = iter(cycle(n))
    return "".join([next(n) if i.isalpha() else i for i in s])
