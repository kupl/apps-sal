# cook your dish here
t = int(input())
for i in range(t):
    c = []
    l = list(map(int, input().split()))
    a = l[0:len(l) - 1]
    d = l[-1]
    for i in a:
        c.append(i * d)
    s = sum(c)
    if s <= 120:
        print('No')
    else:
        print('Yes')
