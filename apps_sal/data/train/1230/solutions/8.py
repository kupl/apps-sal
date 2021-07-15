import sys

n = int(input())
a = [0]*n
if (n > 300):
 print('Yes')
 return
s = input().split()
for i in range(n):
 a[i] = int(s[i]) 
a.sort()
for i in range(n-3):
 for j in range(i+1, n-2):
  for k in range(j+1, n-1):
   x = (a[i]^a[j])^a[k]
   l = k + 1
   r = n - 1
   while r - l > 1:
    c = ( r + l ) / 2
    if a[c] > x:
     r=c
    else:
     l=c
   if ((l > k and a[l] == x) or (a[r]==x)):
    print('Yes')
    return
print('No')
