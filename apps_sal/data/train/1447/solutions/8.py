# your code goes here
def fun(l):
 t=[]
 s=list(set(l))
 for i in s:
  t.append(l.count(i))
 #print(t)
 #print(len(t),len(set(t)))
 if len(t)==len(set(t)):
  #print(1)
  return 1
 #print(0)
 return 0
 
for _ in range(int(input())):
 n=int(input())
 l=[int(i) for i in input().split()]
 s=0
 if fun(l)==0:
  print("NO")
 else:
  for i in range(n-1):
   if l[i]!=l[i+1]:
    s+=1
  if s==len(set(l))-1:
   print("YES")
  else:
   print("NO")
