from fractions import Fraction
from functools import reduce
def product(fracs):
    t = Fraction(reduce(lambda x,y : x*y,fracs))
    return t.numerator, t.denominator
def __starting_point():
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*list(map(int, input().split()))))
    result = product(fracs)
    print((*result))

'''
3
1 2
3 4
10 6
'''

__starting_point()
