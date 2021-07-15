n = int(input())
a = list(map(int,input().split()))
l = []
ans = [0 for i in range(n)]
for i in range(n):
    l.append([a[i],i])
l.sort(key=lambda x:x[1],reverse=True)
l.sort(key=lambda x:x[0],reverse=True)
count = 1
count0 = 0
b = l[0][0]
c = l[0][1]
for i in range(1,n):
    if l[i][0] == b:
        count += 1
        c = min(c,l[i][1])
    else:
        ans[c] += (b-l[i][0])*count
        count += 1
        b = l[i][0]
        c = min(l[i][1],c)
ans[c] += b*count
for i in range(n):
    print(ans[i])
