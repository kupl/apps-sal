from collections import defaultdict
from sys import stdin
inp = stdin.readline


def convert_num(number):
    number_list = list(map(int, number))
    res = ''.join((str(d & 1) for d in number_list))
    return '0' * (18 - len(res)) + res


def convert_pattern(pattern):
    return '0' * (18 - len(pattern)) + pattern


t = int(inp())
multiset = defaultdict(int)
while t:
    t -= 1
    (op, item) = inp().split()
    if op == '+':
        multiset[convert_num(item)] += 1
    elif op == '-':
        multiset[convert_num(item)] -= 1
    else:
        print(multiset[convert_pattern(item)])
