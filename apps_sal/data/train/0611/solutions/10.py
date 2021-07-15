for _ in range(int(input())):
 a = int(input())
 array = list(map(int,input().split()))
 common = list()
 for x in array:
  if array.count(x)>1:
   common.append(x)
 
 if len(common)==0:
  print("Poor Chef")
  continue
 
 ind = dict()
 for x in common:
  if x not in ind:
   ind[x]=list()
  for y in range(len(array)):
   if array[y]==x:
    ind[x].append(y+1)
   
 flag = 0
 for x in ind:
  lis = ind[x]
  for m in lis:
   for n in lis:
    if m!=n and m in array and n in array:
     print("Truly Happy")
     flag = 1
     break
   if flag == 1:
    break
  if flag == 1:
   break
 else:
  if flag == 0:
   print("Poor Chef")
     

