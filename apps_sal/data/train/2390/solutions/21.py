import sys
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    # print(d)
    b = list(dict.values(d))
    c = [0] * n
    ans = 0
    if b[0] == n:
        print(n)
    else:
        for i in range(len(b) - 1, -1, -1):
            if c[b[i]] == 0:
                ans += b[i]
                c[b[i]] = 1
                # print("adfasf")
            else:
                while c[b[i]] == 1:
                    b[i] -= 1
                c[b[i]] = 1
                c[0] = 0
                ans += b[i]
            # print(b[i])
        print(ans)
