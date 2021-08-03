# cook your dish here
for h in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = 0
    if l.count(1) == n:
        print(0)
    else:
        for i in l:
            if i == 0:
                s += 1100
            elif s != 0:
                s += 100
        print(s)
