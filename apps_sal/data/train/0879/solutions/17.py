t = int(input())
for i in range(t):
    (x, y) = list(map(int, input().split()))
    m = x // y
    sum1 = 0
    l = []
    for i in range(1, m + 1):
        n = y * i
        l.append(n)
    for i in range(len(l)):
        q = l[i] % 10
        sum1 = sum1 + q
    print(sum1)
