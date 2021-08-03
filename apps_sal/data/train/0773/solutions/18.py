# cook your dish here
try:
    for _ in range(int(input())):
        n = int(input())
        l = []
        if (n % 2 == 0):
            for i in range(1, n + 1):
                if(i % 2 == 0):
                    l.append(str(i - 1))
                else:
                    l.append(str(i + 1))
        else:
            for j in range(1, n - 1):
                if(j % 2 == 0):
                    l.append(str(j - 1))
                else:
                    l.append(str(j + 1))
            l.append(str(n))
            l.append(str(n - 2))
        print(' '.join(l))
except:
    pass
