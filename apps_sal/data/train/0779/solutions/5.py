#!/usr/bin/python3

ns = lambda: input()
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

for _ in range(ni()):
 n=ni()
 a=nl()
 a.sort()
 ans=a[-1]
 for i in range(1,n):
  ans=(ans+a[n-1-i])/2
 print(ans)
