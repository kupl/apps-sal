try:
    for i in range(int(input())):
        a1 = list(map(int, input().split()))
        a = a1[0]
        d = a1[1]
        k = a1[2]
        n = a1[3]
        inc = a1[4]
        for i in range(1, n):
            if((i) % k == 0):
                d = d + inc
            a = a + d
        print(a)
except:
    pass
