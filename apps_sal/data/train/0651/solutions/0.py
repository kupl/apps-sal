try:
    for i in range(int(input())):
        n = int(input())
        l = [int(j) for j in input().split()][:n]
        d = {}
        for j in l:
            d[j] = d.get(j, 0) + 1
        a = len(d)
        c = 0
        for j in list(d.keys()):
            while(d[j] >= 3):
                d[j] = (d[j] // 3) + (d[j] % 3)
            if(d[j] == 2):
                c = c + 1
        if(c & 1):
            s = 0
            for j in list(d.values()):
                s = s + j
            print(s - c - 1)
        else:
            s = 0
            for j in list(d.values()):
                s = s + j
            print(s - c)
except:
    pass
