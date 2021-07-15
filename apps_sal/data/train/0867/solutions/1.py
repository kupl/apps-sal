T = int(input())
for _ in range(T):
 W = list(map(int, input().strip().split()))
 S = W[0]
 W = W[1:]
 W = W[::-1]
 i = 0
 c = 0
 flag = 0
 while (len(W) != 0 or flag != 1) and i<len(W):
  k = i
  su = 0
  while su <= S and k<len(W)-1:
   su += W[k]
   k += 1
  if su-W[k-1]<=S:
   c += 1
  else:
   flag = 1
  i += 1
 print(c-1) 

