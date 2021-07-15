def chk():
 for r in range(i+1, i+k):
  if m[r][ix:ix+k] != ss:
   return False
 return True 
l, r, q = list(map(int, input().split()))
m = [input().replace(" ", "") for _ in range(l)]
for _ in range(q):
 k, s = input().split()
 k = int(k)
 ss = k * s
 ans = "no"
 for i in range(l-k+1):
  st = 0
  while ss in m[i][st:]:
   ix = m[i].index(ss, st)
   if chk():
    ans = "yes"
    break
   st = ix + 1
  if ans == "yes":break 
 print(ans)
