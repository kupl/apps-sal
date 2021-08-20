def check(s):
    for i in range(len(s) - 1):
        if int(s[i + 1]) < int(s[i]):
            return 1
    return 0


t = int(input())
for i in range(t):
    ok = 0
    n = list(input())
    l = []
    for k in n:
        try:
            l.append(int(k))
        except:
            pass
    while check(l):
        for j in range(len(l) - 1):
            if l[j + 1] < l[j]:
                l[j] = l[j] - 1
                for k in range(j + 1, len(l)):
                    l[k] = 9
                break
    s = ''
    for i in l:
        s += str(i)
    print(int(s))
