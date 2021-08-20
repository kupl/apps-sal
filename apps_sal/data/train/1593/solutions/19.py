t = int(input())
cl = [1, 2, 5, 10, 50, 100]
l = len(cl)
for i in range(t):
    a = int(input())
    n = 0
    w = 1
    while a % cl[-w] != 0:
        n = n + a // cl[-w]
        a = a % cl[-w]
        w = w + 1
    n = n + a // cl[-w]
    print(n)
