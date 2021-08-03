# cook your dish here
n = int(input())
l = [int(i) for i in input().split()]
x = int(input())
l.sort()
if(l[0] >= 0):
    print(0)
else:
    cnt = 0
    cost = 0
    for i in l:
        if(i < 0):
            cnt += 1
        else:
            break
    l = l[0:cnt]
    if(x >= len(l)):
        print(sum(l) * -1)
    else:
        k = min(l[x:len(l)])
        cost += -1 * k * x
        tmp = l[0:x]
        tmp = [i - k for i in tmp]
        for i in tmp:
            cost += max(0, -1 * i)
        print(cost)
