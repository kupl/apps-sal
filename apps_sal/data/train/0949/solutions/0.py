def check(l, n):
    m = 0
    for i in range(n - 1):
        x = l[i]
        c = 0
        j = i
        while (j + 2 < n and l[j + 2] == x) or (j + 1 < n and l[j + 1] == x):
            if l[j + 1] == x:
                j = j + 1
            else:
                j += 2
            c += 1
        if m < c:
            m = c
    return m


t = int(input())
for _ in range(t):
    no = int(input())
    a = list(map(int, input().split()))
    print(check(a, no))
