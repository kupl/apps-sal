n = int(input())
a = list(map(int,input().split()))
l = [0]
ind = [-1]
for i in range(n):
    if a[i] > l[-1]:
        l.append(a[i])
        ind.append(i)
c1 = [0]*(len(l)+1)
c2 = [0]*(len(l)+1)
c1[0] = n
a.sort()
now = 0
for i in a:
    while now < len(l) and l[now] <= i:
        now += 1
    c1[now] -= 1
    c2[now-1] += i-l[now-1]
ans = [0]*n
for i in range(1,len(l)):
    c1[i] += c1[i-1]
    count = (l[i]-l[i-1])*c1[i]+c2[i-1]
    ans[ind[i]] = count

for i in ans:
    print(i)

