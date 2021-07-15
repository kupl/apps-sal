# cook your dish here
t = int(input())

for _ in range(t):
 n = int(input())
 
 a = [int(x) for x in input().split()]
 b = [int(x) for x in input().split()]
 
 a.sort()
 b.sort()
 
 ans = 0
 for i in range(n):
  ans += min(a[i],b[i])
  
 print(ans)
