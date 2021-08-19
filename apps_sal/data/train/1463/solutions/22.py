t = int(input())
while t > 0:
    n = int(input())
    if n == 1:
        print(1)
        print(1, 1)
    else:
        print(n // 2)
        l = []
        for i in range(1, n, 2):
            l.append([i, i + 1])
        if n % 2 != 0:
            l[-1].append(n)
            for i in range(len(l) - 1):
                print(2, *l[i])
            print(3, *l[-1])
        else:
            for i in l:
                print(2, *i)
    t -= 1
