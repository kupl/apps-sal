# cook your dish here
for u in range(int(input())):
    n = int(input())
    l = []
    x = 0
    f = []
    for i in range(n + 1):
        f.append(' ')
    for i in range(n + 1):
        f = []
        for i in range(n + 1):
            f.append(' ')
        for j in range(x, n + 1):
            f[j] = str(j)
        x += 1
        l.append(f)
    d = l[1:][::-1]
    for i in d:
        print(''.join(i))
    for i in l:
        print(''.join(i))
