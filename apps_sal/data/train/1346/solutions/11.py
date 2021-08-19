t = int(input())
for i in range(t):
    lst = input().split()
    n = int(lst[0])
    w = int(lst[1])
    res = 0
    m = 10 ** 9 + 7
    for j in range(1, 10):
        for k in range(10):
            if k - j == w:
                res += 1
    print(res * 10 ** (n - 2) % m)
