from collections import Counter
t = int(input())
for i in range(t):
    s = input()
    c = Counter(s)
    l = []
    for item in list(c.keys()):
        if(c[item] >= 2):
            l.append(item)
            l.append(item)
        else:
            l.append(item)
    l = [int(k) for k in l]
    ans = ""

    for j in range(len(l)):
        for k in range(j + 1, len(l)):
            a = 10 * l[j] + l[k]
            b = 10 * l[k] + l[j]
            if(a >= 65 and a <= 90):
                ans += str(chr(a))
            if(b >= 65 and b <= 90):
                ans += str(chr(b))
    c = Counter(ans)
    l = list(c.keys())
    l.sort()
    ans = ''
    for item in l:
        ans += item
    print(ans)
