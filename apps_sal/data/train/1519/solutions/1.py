t = int(input())
don = 2
for i in range(t):
    x = int(input())
    n = 1
    while pow(2, n) < x:
        n += 1
    don = pow(2, n)
    print(don)
