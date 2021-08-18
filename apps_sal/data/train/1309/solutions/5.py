t = int(input())
for i in range(t):
    n = int(input())
    if(n == 1):
        print(1)
    else:
        a = ""
        l = 0
        for k in range(n):
            a = ""
            a = a + '*' * l
            for j in range(n - l, 0, -1):
                a = a + str(j)
            l += 1
            print(a)
