mod = 10**9 + 7
for _ in range(int(input())):
    n, m = map(int, input().split())
    num = n // 2
    tot = (num * (2 + 2 * num)) // 2
    print(pow(m, tot, mod))
