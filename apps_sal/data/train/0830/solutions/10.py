'''for _ in range(int(input())):
    N = int(input())
    a = list(input())
    b = list(input())
    aset = set(a)
    bset = set(b)
    if(a == b):
     print(0)

    elif(bset.issubset(aset)):
     d = {}
     wr = {}
     f = 0
     for i in range(N):
      if(a[i] != b[i]):
       if b[i] in d:
        d[b[i]].append(i)
        wr[b[i]].append(a[i])
       else:
        d[b[i]] = []
        wr[b[i]] = []
        d[b[i]].append(i)
        wr[b[i]].append(a[i])
     #print(wr,d)

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
       print(d[k],a.index(k))



    else:
     print(-1)''' 


for _ in range(int(input())):
 n=int(input())
 
 a=list(input())
 
 b=list(input())
 if(a==b):
  print(0)
 else:
  l=[]
  c=0
  for i in range(n):
   if(b[i] not in l):
    if(b[i] not in a):
     c=1
     break
    l.append(b[i])
  if(c):
   print(-1)
  else:
   l.sort()
   l.reverse()
   truthy=0
   list1=[]
   for i in range(len(l)):
    current=l[i]
    posb=[]
    one=None
    for j in range(n):
     if(one==None):
      if(a[j]==current):
       one=j
     if(b[j]==current):
      posb.append(j)
    for j in range(len(posb)):
     if(a[posb[j]]<current):
      truthy=1
      break
    if(truthy==1):
     break
    else:
     
     if(one not in posb):
      posb.append(one)
     qq=0
     for j in range(len(posb)):
      if(a[posb[j]]!=current):
       qq=1
     if(qq):
      for j in range(len(posb)):
       a[posb[j]]=current
      list1.append(posb)
   if(truthy):
    print(-1)
   else:
    print(len(list1))
    for i in range(len(list1)):
     print(len(list1[i]),end=" ")
     for j in range(len(list1[i])):
      print(list1[i][j],end=" ")
     print("\n")
