t = int(input())
for _ in range(t):
    s = input()
    r = input()
    ans = 1000000000000000
    c = 0
    l = 0
    k = 0
    for i in range(len(s)):
        if s[i] != r[i]:
            c += 1
            l += 1
            if c == 1:
                k += 1
        else:
            c = 0
    a = 0
    b = 0
    ans = k * l
    for i in range(len(s) - 1, -1, -1):
        if s[i] != r[i]:
            b = i
            break
    for i in range(len(s)):
        if s[i] != r[i]:
            a = i
            break
    gap = []
    c = 0
    for i in range(a, b + 1):
        if s[i] == r[i]:
            c += 1
        elif c != 0:
            gap.append(c)
            c = 0
    gap.sort()
    for i in gap:
        k -= 1
        l += i
        ans = min(ans, k * l)
    print(ans)
