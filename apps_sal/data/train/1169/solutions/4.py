import string
t = int(input().strip())
for _ in range(0, t):
    a = input().strip()
    b = input().strip()
    d = {}
    e = {}
    la = 0
    lb = 0
    for i in a:
        i = i.upper()
        if i == ' ':
            continue
        try:
            d[i] += 1
        except:
            d[i] = 1
        la += 1
    for i in b:
        i = i.upper()
        if i == ' ':
            continue
        try:
            e[i] += 1
        except:
            e[i] = 1
        lb += 1
    left = la + lb
    for i in d:
        try:
            e[i] += 0
        except:
            continue
        if d[i] < e[i]:
            left -= 2 * d[i]
        else:
            left -= 2 * e[i]
    f = ['F', 'L', 'A', 'M', 'E', 'S']
    old = 0
    for q in range(0, 5):
        old = ((left % (6 - q) + old) % (6 - q) - 1) % (6 - q)
        f.pop(old)
    ans = {'F': 'FRIENDS', 'L': 'LOVE', 'A': 'ADORE', 'M': 'MARRIAGE', 'E': 'ENEMIES', 'S': 'SISTER'}
    print(ans[f[0]])
