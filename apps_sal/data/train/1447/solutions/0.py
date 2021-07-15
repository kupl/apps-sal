# cook your dish here
 
for __ in range(int(input())):
 n=int(input())
 arr=list(map(int,input().split()))
 d={}
 s=set()
 flag=0
 for i in range(n):
  if arr[i] in list(d.keys()):
   d[arr[i]]+=1
  else:
   d[arr[i]]=1
  curr_ele=arr[i]
  if (curr_ele in s) and arr[i-1]!=arr[i]:
   flag=1
   break
  else:
   s.add(arr[i])
 c=list(d.values())
 if len(c)!=len(set(c)):
  flag=1
 if flag==1:
  print("NO")
 else:
  print("YES")
 
   
  
 

