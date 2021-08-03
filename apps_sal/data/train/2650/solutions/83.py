import math
from datetime import date


def main():

    line = input().split()
    n = int(line[0])
    k = int(line[1])

    a = []
    for i in range(n):
        s = input()
        a.append(s)

    ans = ""
    for x in sorted(a):
        ans += x

    print(ans)


main()
