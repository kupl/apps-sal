from math import sqrt


def solve():
    (a, m) = list(map(int, input().split()))
    all_vals = []
    for i in range(1, int(sqrt(m)) + 1):
        if m % i == 0:
            if (m - i) % a == 0 and (m - i) // a % i == 0:
                all_vals.append((m - i) // a)
            i = m // i
            if i != m and (m - i) % a == 0 and ((m - i) // a % i == 0):
                all_vals.append((m - i) // a)
    print(len(all_vals))
    if len(all_vals) != 0:
        all_vals.sort()
        print(*all_vals)


for T in range(int(input())):
    solve()
