# cook your dish here
for u in range(int(input())):
    l = list(map(int, input().split()))
    n = len(l)
    s = 0
    for i in range(n):
        if(l[i] > 30):
            s = s + 1
    c = 0
    x = 0
    for i in range(n):
        if(l[i] % 2 == 0):
            c = c + (l[i] * (i + 1))
            x = x + (i + 1)
    print(s, end=" ")
    ss = c / x
    print('%.2f' % ss)
