import sys
read = sys.stdin.readline
n = int(read())
a = list(map(int , read().split()))
b = list(map(int , read().split()))
presb  = []
pref = 0
for ele in  b:
    pref += ele
    presb.append(pref)
maxj = [0]*n
maxi = [0]*n
maxj[0] = a[0]-presb[0]
for i in range(1,n):
    maxj[i] = max(maxj[i-1],a[i]-presb[i])
maxi[0] = a[0]
for j in range(1,n):
    maxi[j] = max(maxi[j-1],a[j]+presb[j-1])
ans = a[0]
for i in range(1,n):
    ans = max(ans,a[i],a[i]+presb[i-1]+maxj[i-1],a[i]+presb[n-1]-presb[i]+maxi[i-1])
print(ans)
