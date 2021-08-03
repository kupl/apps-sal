def g(n):
    s = list(map(int, input().split()))
    count = 1
    l = []
    i = 0
    iter = 0
    while i < n:
        count = 1
        for j in range(i + 1, n):
            if s[j] * s[j - 1] < 0:
                count += 1
            else:
                break
        while count > 0:
            l.append(count)
            count -= 1
            i += 1
    if len(l) != n:
        l.append(1)
    return " ".join(str(i) for i in l)


t = int(input())
for i in range(t):
    n = int(input())
    print(g(n))
