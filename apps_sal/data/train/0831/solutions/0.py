for _ in range(int(input())):
    (n, m) = input().split()
    (n, m) = (int(n), int(m))
    x = y = c = 0
    l = list(map(int, input().split()))
    for i in range(n):
        for j in range(i, n):
            x = x + l[j]
            if x % m > y:
                y = x % m
                c = 1
            elif y == x % m:
                c += 1
        x = 0
    print(y, c)
