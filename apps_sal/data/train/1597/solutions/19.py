from sys import stdin, stdout
import math


def Divisors(n):
    l = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                l.append(i)
            else:
                l.append(n // i)
                l.append(i)
    return l


for _ in range(int(input())):
    a, m = list(map(int, input().split()))
    div = Divisors(m)
    ans = set()
    for i in div:
        if ((m // i) - 1) % a == 0:
            ans.add((((m // i) - 1) // a) * i)
    ans = list(ans)[1:]
    ans.sort()
    print(len(ans))
    print(*ans)
