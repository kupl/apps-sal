for _ in range(int(input())):
    a = [0 for i in range(32)]
    m, n = list(map(int, input().split()))
    k = 0
    while m != 0:
        a[k] = m % 2
        k += 1
        m = m // 2
    for i in range(n):
        c = int(input())

        if c == 4:
            p, q = list(map(int, input().split()))
            a[p - 1], a[q - 1] = a[q - 1], a[p - 1]
        if c == 1:
            d = int(input())
            if a[d - 1] == 1:
                print("ON")
            else:
                print("OFF")

        if c == 2:
            d = int(input())
            a[d - 1] = 1
        if c == 3:
            d = int(input())
            a[d - 1] = 0
