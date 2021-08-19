import sys


def solve():
    r = list(map(int, input().split()))
    n = r[0]
    k = r[1]
    l = list()
    l.append(1)
    c = k
    justI = 0
    maxsofar = 1
    for i in range(1, n):
        if justI == 1:
            l.append(maxsofar + 1)
            maxsofar += 1
        else:
            l.append(l[i - 1] + c)
            maxsofar = max(maxsofar, l[i - 1] + c)
            if c > 1:
                c -= 1
                c *= -1
            elif c < -1:
                c += 1
                c *= -1
            else:
                justI = 1
    return l


def read(mode=2):
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return list(map(int, inputs.split()))


def write(s='\n'):
    if s is None:
        s = ''
    if isinstance(s, list):
        s = ' '.join(map(str, s))
    if isinstance(s, tuple):
        s = ' '.join(map(str, s))
    s = str(s)
    print(s, end='')


def run():
    if sys.hexversion == 50594544:
        sys.stdin = open('test.txt')
    res = solve()
    write(res)


run()
