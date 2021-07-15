#this time it will work
try:
    n = int(input())
    l = list(map(int , input().split()))
except:
    return
ans = [0] * n
anss = [0] * n
ans[0] = l[0]
ans[1] = l[1]
for i in range(2,n):
    ans[i] = min(ans[i-1],ans[i-2]) + l[i]
l.reverse()
anss[0] = l[0]
anss[1] = l[1]
for i in range(2,n):
    anss[i] = min(anss[i-1],anss[i-2]) + l[i]
print(min(ans[-1],anss[-1]))


