for _ in range(int(input())):
 l=list(input())
 l2=[]
 for i in l:
  if i not in l2:
   l2.append(i)
 print(len(l2))
