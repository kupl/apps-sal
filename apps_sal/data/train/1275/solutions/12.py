for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    m = list(map(int, input().split()))
    m.sort()
    sm = m[0]
    bg = m[-1]
    for i in range(n):
        print(max(abs(i - sm), abs(i - bg)), end=' ')
    print()
