from sys import stdin
from math import ceil, gcd

# Input data
#stdin = open("input", "r")


def func():

    return


t = int(stdin.readline())
for _ in range(t):
    x1, y1, x2, y2 = list(map(int, stdin.readline().split()))
    print("Test case : {}".format(_ + 1))
    for i in range(int(stdin.readline())):
        x, y = list(map(int, stdin.readline().split()))
        if x1 == x2:
            if x == x1:
                print("YES")
            else:
                print("NO")
                d = abs(x - x1)
                d = str(d) + '.000000'
                print(d)
        else:
            m = (y2 - y1) / (x2 - x1)
            c = y1 - (m * x1)
            if y == (m * x) + c:
                print("YES")
            else:
                print("NO")
                d = abs(y - (m * x) - c) / ((1 + m**2)**0.5)
                d = str(round(d, 6))
                for i in range(len(d)):
                    if d[i] == '.':
                        pos = i
                        break
                if len(d) - pos - 1 == 6:
                    print(d)
                else:
                    d += '0' * (7 - len(d) + pos)
                    print(d)
