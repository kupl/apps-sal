n = int(input())
a = [0]*1000001
b = [0]*1000001
for i in range(n):
  l = list(map(int,input().split()))
  a[l[0]] = 1
  b[l[0]] = l[1]
  
notdestroyed = [0]*1000001
if a[0] == 1:
  notdestroyed[0] = 1
for i in range(1,1000001):
  if a[i] == 1:
    notdestroyed[i] = notdestroyed[i-b[i]-1]+1
  else:
    notdestroyed[i] = notdestroyed[i-1]
    
print(n-max(notdestroyed))
