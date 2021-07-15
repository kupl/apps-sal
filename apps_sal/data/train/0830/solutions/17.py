# cook your dish here
for _ in range(int(input())):
 n = int(input())
 firstString = list(input())
 secondString = list(input())
 firstStringSet = set(firstString)
 secondStringSet = set(secondString)
 if firstString==secondString:
  print(0)
 
 elif secondStringSet.issubset(firstStringSet):
  d={}
  wr = {}
  f=0
  for i in range(n):
   if firstString[i]!=secondString[i]:
    if secondString[i] in d:
     d[secondString[i]].append(i)
     wr[secondString[i]].append(firstString[i])
    else:
     d[secondString[i]]=[]
     wr[secondString[i]]=[]
     d[secondString[i]].append(i)
     wr[secondString[i]].append(firstString[i])

  # print(wr,d)
  for k,v in sorted(wr.items(),reverse=True):
   # print(k,v)
   for i in v:
    # print(k,i)
    if ord(k)>ord(i):
     f=1
     break
   if f==1:
    break
  # print(flag)
  if f==1:
   print(-1)
  else:
   print(len(d))
   for k,v in sorted(d.items(),reverse=True):
    print(len(d[k])+1,end=" ")
    print(*d[k],firstString.index(k))
  
  
 else:
  print(-1)
