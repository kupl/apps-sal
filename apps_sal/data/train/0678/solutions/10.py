for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = [l[0]] + [0] * (n - 1)
    for i in range(1, n):
        s[i] = s[i - 1] + l[i]
    a = 1
    x = s[0] + 1
    while x < n:
        a = a + 1
        x = x + s[x - 1]
    print(a)
