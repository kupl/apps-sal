from functools import reduce
from operator import add
import re


P_TO_PYTHON   = re.compile(r'[+-]?\d*i')
P_FROM_PYTHON = re.compile(r'[()]|\b1(?=j)|([+-]|^)0j')

complexify=lambda m: "{}{}1j".format(m.group()[:-1], '*' * (len(m.group()) > 1 and m.group()[-2] not in "-+"))

def complexSum(arr):
    lst = [P_TO_PYTHON.sub(complexify, s) for s in arr]
    cpx = reduce(add, map(eval, lst), 0)
    return P_FROM_PYTHON.sub('', str(cpx)).replace('j','i')
