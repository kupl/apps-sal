mod = 10**9 + 7
for t in range(int(input())):
 n, k = list(map(int, input().split()))
 a = list(map(int, input().split()))
 ans = 0
 temp = 1
 limit = min(n,k)+1
 c = a.count(0)
 if (c == 0):
  x = k%2
  for i in range(0, limit):
   if (i%2 == x):
    ans += temp
    ans %= mod
   temp = (temp * (n-i)) / (1+i)
 else:
  n = n-c
  for i in range(0, limit):
   ans += temp
   ans %= mod
   temp = (temp * (n-i)) / (1+i)
 print(ans) 
