# cook your dish here
for _ in range(int(input())):
    A = int(input())
    x = 1
    pro = 0
    n = 0
    d = 1
    s = 0
    while True:
        n += 1
        s += x
        y = A * n - s
        if pro < y:
            pro = y
            d = n
        if y < 0:
            break
        x = x * 2
    print(n - 1, d)
