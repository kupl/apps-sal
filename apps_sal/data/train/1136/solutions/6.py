def Solve2():
    (n, m) = map(int, input().split())
    if n % 2 == 1:
        print((n // 2 + 1) * m)
    else:
        print(n // 2 * m)


for _ in range(int(input())):
    Solve2()
