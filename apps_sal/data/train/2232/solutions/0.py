"""
Codeforces Round 372 Div 1 Problem A

Author  : chaotic_iak
Language: Python 3.5.2
"""


def main():
    (n,) = read()
    curr = 2
    for lv in range(1, n + 1):
        tgt = (lv * (lv + 1)) ** 2
        print((tgt - curr) // lv)
        curr = lv * (lv + 1)
    return


def read(typ=int):
    input_line = input().strip()
    if typ is None:
        return input_line
    return list(map(typ, input_line.split()))


def write(s='\n'):
    if s is None:
        s = ''
    if isinstance(s, list):
        s = ' '.join(map(str, s))
    s = str(s)
    print(s, end='')


write(main())
