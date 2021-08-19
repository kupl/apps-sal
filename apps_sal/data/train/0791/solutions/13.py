t = int(input())
while t != 0:
    (n, d) = list(map(int, input().strip().split()))
    a = input().strip()
    a = a.split()
    c = 0
    b = []
    c = sum((int(i) for i in a))
    if c % n != 0:
        print('-1')
    else:
        m = 0
        b += n * [c / n]
        f = 1
        for i in range(0, len(a) - d):
            if a.count(a[0]) == len(a):
                f = 0
                break
            elif int(a[i]) > int(b[i]):
                temp = int(a[i]) - int(b[i])
                a[i] = int(b[i])
                a[i + d] = int(a[i + d]) + temp
                m = m + temp
            elif int(a[i]) < int(b[i]):
                temp = int(b[i]) - int(a[i])
                a[i] = int(b[i])
                a[i + d] = int(a[i + d]) - temp
                m = m + temp
            if i == len(a) - d - 1 and all((int(x) == int(a[0]) for x in a)):
                f = 0
        if f == 0:
            print(m)
        else:
            print('-1')
    t = t - 1
