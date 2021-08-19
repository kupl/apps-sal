import sys


def input():
    return sys.stdin.readline().strip()


ipnut = input


def main(t=1):
    for i in range(t):
        n = int(input())
        a = []
        b = []
        s = list(map(int, input()))
        f = False
        for i in s:
            if i == 0:
                a.append(0)
                b.append(0)
            elif i == 1 and (not f):
                a.append(1)
                b.append(0)
                f = True
            elif i == 1:
                a.append(0)
                b.append(1)
            elif f:
                a.append(0)
                b.append(2)
            else:
                a.append(1)
                b.append(1)
        print(''.join(map(str, a)))
        print(''.join(map(str, b)))


main(int(input()))
