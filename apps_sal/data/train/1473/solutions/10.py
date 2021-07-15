
def solve(r, c, ar ):
 
 if not r*c == ar[0] + ar[1] + ar[2]:
  return "No"
 
 if ar[0] % r == ar[1] % r == ar[2] % r == 0:
  if ar[0] / r + ar[1] / r + ar[2] / r == c:
   return "Yes"
  
 if ar[0] % c == ar[1] % c == ar[2] % c == 0:
  if ar[0] / c + ar[1] / c + ar[2] / c == r:
   return "Yes" 
  
 for i in range(len(ar)):
  if ar[i] % r == 0:
   cnt = 0
   sml = 0
   sma = 0
   c2 = c - ar[i] / r
   for j in range(len(ar)):
    if i == j:
     continue
    if ar[j] % c2 == 0:
     cnt += 1
     sml += ar[j] / c2
     sma += ar[j]
   if cnt == 2 and sml == r:
    if sma + ar[i] == r * c:
     return "Yes"
  if ar[i] % c == 0:
   cnt = 0
   sml = 0
   sma = 0
   r2 = r - ar[i] / c
   for j in range(len(ar)):
    if i == j:
     continue
    if ar[j] % r2 == 0:
     cnt += 1
     sml += ar[j] / r2
     sma += ar[j]
   if cnt == 2 and sml == c:
    if sma + ar[i] == r * c:
     return "Yes" 
 return "No"
   
  
for cas in range(eval(input())):
 r, c, m, k, j = list(map(int, input().strip().split()))
 print(solve( r, c, [m, k, j] ))
 
 

