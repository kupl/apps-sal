for _ in range(int(input())):
 n = int(input())

 arr= list(map(int,input().split()))
 arr.sort()
 d={}
 for i in arr:
  if i not in d:
   d[i]=1
  else:
   d[i]+=1
 
 flag = True
 for i in d:
  if d[i]>2:
   flag=False
   break
 
  

 if arr.count(max(arr))!=1:
  flag=False
 
  
 if flag==True:

  arr1=[]
  arr2=[]
  for i in d:
   if d[i]<=2:
    if d[i]==2:
     
     arr2.append(i)
    arr1.append(i)
  arr2.reverse()
  rearr= arr1+arr2

  print("YES")
  print(*rearr)

 else:
  print("NO")
 
# cook your dish here

