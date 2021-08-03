# cook your dish here
t = int(input())
for i in range(0, t):
    k = int(input())
    b = []
    for j in range(k, -1, -1):
        a = []
        s = ' '
        a.append(str(s * j))
        for m in range(k, j - 1, -1):
            a.append(str(m))
        x = ''.join(a)
        b.append(x)
        print(*a, sep='')
    b.reverse()
    b.pop(0)
    print(*b, sep='\n')
