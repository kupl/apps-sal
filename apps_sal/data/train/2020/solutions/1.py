from fractions import gcd
from functools import reduce


LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def necklace_odd(a):
    oi = next(i for i, ai in enumerate(a) if ai%2)
    o = a[oi]
    g = reduce(gcd, a)
    s = [LETTERS[i] * (a[i]//(2*g)) for i in range(len(a)) if i != oi]
    return g, (''.join(s) + (LETTERS[oi]*(o//g)) + ''.join(reversed(s))) * g


def necklace_even(a):
    g = reduce(gcd, a)//2
    s = [LETTERS[i]*(a[i]//(2*g)) for i in range(len(a))]
    return 2*g, (''.join(s) + ''.join(reversed(s))) * g


def necklace(a):
    if len(a) == 1:
        return a[0], LETTERS[0]*a[0]

    nodd = sum(ai%2 for ai in a)
    if nodd > 1:
        return 0, ''.join(LETTERS[i]*a[i] for i in range(len(a)))

    return (necklace_odd if nodd else necklace_even)(a)


def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n
    k, e = necklace(a)
    print(k)
    print(e)




# Made By Mostafa_Khaled

__starting_point()
