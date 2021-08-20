from operator import gt
from numpy import sign
result = {-1: 'Bob made "Jeff" proud!', 0: 'that looks like a "draw"! Rock on!', 1: 'Alice made "Kurt" proud!'}


def solve(a, b):
    alice = sum(map(gt, a, b))
    bob = sum(map(gt, b, a))
    return f'{alice}, {bob}: {result[sign(alice - bob)]}'
