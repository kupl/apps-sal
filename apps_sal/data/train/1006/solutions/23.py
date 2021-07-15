# your code goes here
# your code goes here
for _ in range(int(input())):
 n,d=map(int,input().split())
 l=list(map(int,list(str(n))))
 if l==sorted(l):
  a=[x for x in l if x<=d]
  l=a+[d]*(len(l)-len(a))
 else:
  i=0
  while(True):
   if l[i]>l[i+1]:
    l.pop(i)
    l.append(d)
    i=0
   else:
    i+=1
   if l==sorted(l):
    break
 l=list(map(str,l)) 
 print(int("".join(l)))
