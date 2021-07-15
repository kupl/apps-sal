def find_final_posi(l1, cp, jumps):
 count = 0
 i = cp
 while i in range(cp, cp + 101):
  if ((count == jumps) | (i>=len(l1))):
   return cp
  elif l1[cp] < l1[i]:
   cp = i
   i += 1
   count += 1
  else:
   i += 1
 return cp

[n,q]=[int(x) for x in input().split()]
inp=[int(x) for x in input().split()]
hillht=[-1]
hillht.extend(inp)
for j in range(q):
 oper=[int (x) for x in input().split()]
 if oper[0]==2:
  for x in range(oper[1],oper[2]+1):
   hillht[x]+=oper[3]
 else:
  i = oper[1]
  k = oper[2]
  l=i
  signal=0
  print(find_final_posi(hillht,i,k))
