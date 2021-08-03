for _ in range(int(input())):
    n = int(input())
    a = []
    for _ in range(1, n + 1):
        a.append(str(_))
    a = a + a
    for _ in range(n):
        print(''.join(a[_:_ + n]))
