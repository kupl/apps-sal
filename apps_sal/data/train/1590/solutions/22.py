# cook your dish here
try:
    t = int(input())
    for i in range(t):
        l = list(map(int, input().split()))
        r = l.index(max(l))
        s = 0
        for j in l:
            if(j != l[r]):
                s += j
        if(s + 1 >= l[r]):
            print("Yes")
        else:
            print("No")
except:
    pass
