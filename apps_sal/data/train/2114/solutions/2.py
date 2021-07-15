n,m = [int(x) for x in input().split()]

l = [int(x) for x in input().split()]

x = 0;
for i in range(m):
    a,b,c = [int(x) for x in input().split()]
    cur = (l[a-1]+l[b-1])/c
    #print(a,b,c,cur)
    if cur > x: x = cur
print("%0.15f"%x)

