# cook your dish here
t = int(input())
while(t > 0):
    num, d = input().split()
    a = list(map(int, num))
    mi = min(a)
    d = int(d)

    l = len(a)
    l1 = l
    if mi < d:
        last = l - a[::-1].index(mi) - 1
        c = 0
        while(last < l):

            cmi = a.count(mi)
            for k in range(cmi):
                print(mi, end='')
                c = c + 1
            if(last == l - 1):
                break
            a = a[last + 1:]
            mi = min(a)
            if(mi >= d):
                break
            l = len(a)
            last = l - a[::-1].index(mi) - 1

        while c < l1:
            print(d, end='')
            c = c + 1

    else:
        for i in range(l1):
            print(d, end='')
    print()
    t = t - 1
