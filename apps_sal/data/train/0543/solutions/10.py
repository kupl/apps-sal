# cook your dish here
try:
    for _ in range(int(input())):
        c, d = 0, 0
        t1 = int(input())
        r1 = list(map(int, input().split()))
        d1 = int(input())
        r2 = list(map(int, input().split()))
        t2 = int(input())
        r3 = list(map(int, input().split()))
        d2 = int(input())
        r4 = list(map(int, input().split()))
        for i in range(t2):
            a = r3[i]
            if a in r1:
                c = c + 1
        for i in range(d2):
            b = r4[i]
            if b in r2:
                d = d + 1
        if c == len(r3) and d == len(r4):
            print("yes")
        else:
            print("no")
except:
    pass
