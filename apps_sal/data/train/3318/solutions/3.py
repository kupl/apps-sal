from itertools import zip_longest
def help(n): return map(int, reversed(str(n)))


def number_of_carries(a, b):
    carry = res = 0
    for x, y in zip_longest(help(a), help(b), fillvalue=0):
        tmp = x + y + carry
        res += tmp > 9
        carry = tmp // 10
    return res
