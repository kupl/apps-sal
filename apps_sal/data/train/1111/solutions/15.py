# cook your dish here
t = int(input())
while t>0:
 n = int(input())
 a = list(map(int, input().split()))
 cnt = 0
 for i in range(n):
  if a[i]%2!=0:
   cnt = cnt + 1
 ans = n - cnt
 print(ans*cnt)
 t = t-1

