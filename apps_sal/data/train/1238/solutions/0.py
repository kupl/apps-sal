test=int(input())
for i in range(test):
 N=input()
 X=[]
 list2=[]
 for x in N:
  X.append(x)
 list1=[]
 list1=list(set(X))
 output=''
 for x in list1:
  for y in X:
   if int(x)>=6:
    n=int(x)*10+int(y)
    list2.append(n)
 for j in list1:
  if int(j)>=6:
   m=int(j)*10+int(j)
   list2.remove(m)
 list2.sort()
 if len(list2)==0:
  print(" ")
 else:
  list2.sort()
  for k in list2:
   if chr(k) not in output and 64<k<91:
    output+=chr(k)
  print(output)
 

