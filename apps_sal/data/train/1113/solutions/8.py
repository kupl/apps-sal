t = int(input())
while t:
    t-=1
    n = int(input())
    l = list(map(int, str(input()).split()))
    k = set(l)
    maxi = 0
    num = 10001
    for i in k:
        c = l.count(i)
        if c>maxi:
            maxi = c
            num = i
        elif c == maxi and i<num:
            num = i
    print(num, maxi)

