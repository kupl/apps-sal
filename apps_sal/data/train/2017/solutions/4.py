import sys

n = int(input())
n *= 2
a = list(map (int, input().split()))
res = 0
for i in range (0, n, 2):
  if a[i] != a[i+1]:
    t = a[i]
    for j in range (i+1, n):
      if a[j] == t:
        for k in range (j, i + 1, -1):
          a[k], a[k-1] = a[k-1], a[k]
          res += 1
        break
   
#print (a)    
print (res)
