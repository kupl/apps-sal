t = int(input())
for _ in range(t):
    s = input()
    l, d, m = 0, 0, 0
    for i in range(len(s)):
        if s[i] == '.':
            l += 1
        if s[i] == '
           if l > m:
                d += 1
                m = l
            l = 0
    print(d)
