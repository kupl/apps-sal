for _ in range(int(input())):
 s = input()
 r = input()
 unlike = []
 curr=None
 l = 0
 k = 0
 for i in range(len(s)):
  if r[i]!=s[i]:
   l += 1
   if curr:
    unlike.append(curr)
    k+=1
   curr = 0
  else:
   if curr!=None:
    curr += 1
 k += 1
 unlike.sort()
 mini = k*l
 for i,j in enumerate(unlike):
  k-=1
  l+=j
  mini = min(mini,k*l)
 print(mini)
