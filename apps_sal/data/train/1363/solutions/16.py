test = eval(input())
while test:
    test = test - 1
    (n, d) = list(map(int, input().split()))
    num = 0
    for i in range(n):
        num = num * 10 + d
    sqr = num ** 2
    s = sqr.__str__()
    l = len(s)
    ans = 0
    for i in range(l):
        ans = (ans + 23 ** i * int(s[i])) % 1000000007
    print(ans)
