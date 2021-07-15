import re
from itertools import zip_longest
def solve(eq):
    val=re.split('[+-/*]',eq)[::-1]
    symb=re.findall('[+-/*]',eq)[::-1]
    return ''.join(i+j for i,j in zip_longest(val,symb,fillvalue=''))

