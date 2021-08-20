t = int(input())
for i in range(t):
    l = [1, 0, 3, 3, 3, 3, 3, 4, 3, 4]
    n = int(input())
    s = 1
    while n > 0:
        s *= l[int(n % 10)]
        n /= 10
    print(s)
