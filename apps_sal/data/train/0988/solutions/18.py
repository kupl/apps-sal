

twopow = {}
for i in range(31):twopow[i] = 2**i
for _ in range(int(input())):
 n,a,b,original_tot = int(input()),list(map(int, input().split())),dict(),0
 for i in range(31):b[i] = 0
 for i in range(n):
  s = bin(a[i])[2:][::-1];
  original_tot += a[i]
  for i in range(len(s)):
   if s[i] == '1':b[i] += 1
 change = 0
 for x in b:
  p = b[x]
  if p > 0:
   if p > n - p:change += (p - (n - p)) * (twopow[x])

 original_tot -= change
 print(original_tot)

