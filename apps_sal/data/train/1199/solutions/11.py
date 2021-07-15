t = int(input())
for _ in range(t):
 s, n = map(int,input().split())
 c = 0
 if s == n:
  c = 1
 elif s > n:
  c += s // n
  s = s % n
  if s % 2 == 1:
   c += 1
  if s != 0 and s != 1:
   c += 1
   
 else:
  if s % 2 == 1:
   c += 1
  if s != 0 and s != 1:
   c += 1
  
 print(c)
