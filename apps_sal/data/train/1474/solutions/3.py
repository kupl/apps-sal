for t in range(int(input())):
    n = input()
    s = input().split()
    d = input()
    f = 0
    num = 0
    for i in s:
        z = i.count(d)
        if (z > f):
            f = z
            num = i
    print(num)
