from math import gcd
for _ in range(int(input())):
 n=int(input())
 l=[int(y) for y in input().split(' ')]
 g=l[1]-l[0]
 count=0
 for i in range(1,n):
  g=gcd(g,l[i]-l[i-1])
 g=gcd(g,360-l[n-1]+l[0])
 for i in range(1, n):
  count+=(l[i]-l[i-1])//g-1
 count+=(360-l[n-1]+l[0])//g-1
 print(count)
