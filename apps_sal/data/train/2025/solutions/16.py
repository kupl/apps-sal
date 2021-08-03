n = int(input())
if n == 1:
    print(0)
    print('')
else:
    a = []
    for i in range(2, n + 1):
        x = i
        p = 0
        for j in a:
            if x % j == 0:
                p += 1
            while x % j == 0:
                x = x // j
        if x > 1 or (x == 1 and p == 1):
            a.append(i)
    s = str(a[0])
    L = len(a)
    for j in range(1, L):
        s = s + ' ' + str(a[j])
    print(len(a))
    print(s)
