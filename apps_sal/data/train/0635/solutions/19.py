n,k = map(int,input().split())
l = list(map(int,input().split()))
M = 10**9+7
farr = []
d = {}
for i in l:
 if i in d:
  d[i] = d[i]+1

 else:
  d[i] = 1

for i in d:
 farr.append(d[i])

#print(farr)
cnt = 1
arr = farr.copy()
#print(arr)
#print(sum(arr))
z = 1
while(z <= k):
 if z == 1:
  cnt = (cnt+sum(arr))%M
  #print(cnt)

 else:
  ic = 0
  i = 0
  kc = 0
  while(i < len(farr)):
   kc = arr[i]
   arr[i] = (ic*farr[i])%M
   ic = ic+kc
   cnt = (cnt+arr[i])%M
   i = i+1

 z = z+1

print(cnt%M)
