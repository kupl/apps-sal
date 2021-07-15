def check(r, c, a):
 for i in range(r):
  for j in range(c):
   adj = 4
   if i == 0 or i == r-1:
    adj -= 1
   if j == 0 or j == c-1:
    adj -= 1
   if a[i][j]>=adj:
    return "Unstable"
    
 return "Stable"

for _ in range(int(input())):
 d = input().split()
 r = int(d[0])
 c = int(d[1])
 a = []
 for i in range(r):
  a.append(list(map(int, input().split())))
 print(check(r, c, a))
