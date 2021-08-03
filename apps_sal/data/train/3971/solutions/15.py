import re


def tidyNumber(n):
    return bool(re.fullmatch('0*1*2*3*4*5*6*7*8*9*', str(n)))
