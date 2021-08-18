
t = int(input())
while (t > 0):
    t = t - 1
    n = int(input())
    a = 100000000
    b = 100000000
    for i in range(0, n):
        s = str(input())
        l = s.count('a')
        if (l < a):
            a = l
        l = s.count('b')
        if (l < b):
            b = l
    print(min(a, b))
