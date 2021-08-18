for i in range(int(input())):
    m, n = list(map(int, input().split()))
    if n < 9:
        print(0, 0)
        continue
    k = len(str(n))
    if n == int(str(9) * k):
        ans = k
    else:
        ans = k - 1
    print(m * ans, m)
