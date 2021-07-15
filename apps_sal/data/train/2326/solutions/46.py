# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n,*a = map(int,read().split())

res = [(0,-1)]+[(a[i],i) for i in range(n)]
res.sort()

ans = [0]*n
num = 0
cnt = 0
midx = idx = n-1
v = res[-1][0]

#print(res)
while res:
    #print(num,cnt,idx)
    ans[midx] += (v-res[-1][0])*cnt
    v = res[-1][0]

    while res and res[-1][0]==v:
        ai,idx = res.pop()        
        cnt += 1
    midx = min(midx,idx)

print(*ans,sep="\n")






