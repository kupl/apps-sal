t = int(input())
for _ in range(t):
    s = input()
    x = ''
    i = 0
    ans = 0
    while i < len(s):
        x = s[i]
        c = 1
        i += 1
        while i < len(s) and s[i] == x:
            i += 1
            c += 1
        if c == 1:
            ans += 8
        else:
            ans += 40
    m = 8 * len(s)
    print(m - ans)
