# cook your dish here
from math import sqrt


def solve():
    a, m = list(map(int, input().split()))
    n = m // (a + 1)

    all_vals = []

    while(a * n < m or (a >= int(sqrt(m)) and n <= sqrt(m))):
        if(a * n + ((m - a * n) * (n % (m - a * n) == 0)) == m):
            all_vals.append(n)
        n += 1

    print(len(all_vals))
    if(len(all_vals) != 0):
        print(*all_vals)


for T in range(int(input())):
    solve()
