from math import ceil


def solve():
    a, m = list(map(int, input().split()))
    n = ceil(m / a)

    all_vals = []

    while((a * n + n) >= m):
        if((m - a * n) > 0 and a * n + ((m - a * n) * (n % (m - a * n) == 0)) == m):
            all_vals.append(n)
        n -= 1

    print(len(all_vals))
    if(len(all_vals) != 0):
        print(*all_vals[::-1])


for T in range(int(input())):
    solve()
