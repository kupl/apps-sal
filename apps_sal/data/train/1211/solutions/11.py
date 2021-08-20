t = int(input())
for _ in range(t):
    s = list(input())
    l = []
    for i in range(len(s)):
        if len(l) < 2:
            l.append(s[i])
        elif s[i] == 'c' and len(l) >= 2 and (l[-1] == 'b') and (l[-2] == 'a'):
            l.pop()
            l.pop()
        else:
            l.append(s[i])
    print(''.join(l))
