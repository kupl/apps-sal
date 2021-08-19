def fun(s):
    su = 0
    for (j, i) in enumerate(s):
        if i == '1':
            su += 2 ** j
    return su


for i in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    a = list((str(bin(int(i)))[2:] for i in b))
    m = str(bin(max(b))[2:])
    l = len(m)
    s = ''
    for i in range(l):
        c1 = c2 = 0
        for j in a:
            l1 = len(j)
            if l1 - i - 1 >= 0:
                if j[l1 - i - 1] == '0':
                    c1 += 1
                else:
                    c2 += 1
            else:
                c1 += 1
        if c1 > c2:
            s += '0'
        else:
            s += '1'
    s = fun(s)
    su = 0
    for i in b:
        su += s ^ i
    print(su)
