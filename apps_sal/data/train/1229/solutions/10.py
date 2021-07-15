import math
test=int(input())
for j in range(test):
 a=[int(x) for x in input().split()]
 inputdata=[int(x) for x in input().split()]
 new1=[]
 new2=[]
 count=0
 count1=0
 for i in range(a[0]):
  if i%2==0:
   new1.append(inputdata[i]) 
  else: 
   new2.append(inputdata[i])
 count=sum(new1)
 count1=sum(new2)
 new1.sort(reverse=True)
 new2.sort()
 if count<count1:
  print("YES")
 else:
  for i in range(len(new2)):
   if new1[i]>new2[i] and a[1]:
    temp=new1[i]
    new1[i]=new2[i]
    new2[i]=temp 
    a[1]=a[1]-1
   if a[1] is 0:
    break;            
  count=sum(new1)
  count1=sum(new2)
  if count<count1:
   print("YES")
  else: print("NO")
