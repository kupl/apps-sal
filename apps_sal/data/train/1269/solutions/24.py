# cook your dish here
t = int(input())
for _ in range(t):
 n = int(input())
 a = list(map(int, input().split()))
 b = list(map(int, input().split()))
 a.sort()
 b.sort()
 tot = 0
 for i in range(n):
  tot = tot + min(a[i],b[i])
 print(tot)
  

