T = int(input())
for i in range(T):
 N = int(input())
 seq = [int(s) for s in input().split()]
 ans = 0
 for i in range(len(seq)):
  a = seq[i]
  c = seq[a-1]
  for j in range(i+1, len(seq)):
   b = seq[j]
   d = seq[b-1]
   if(a!=b and c==d):
    ans = 1
    break
  if(ans == 1):
   break
 if(ans == 1):
  print("Truly Happy")
 else:
  print("Poor Chef")
