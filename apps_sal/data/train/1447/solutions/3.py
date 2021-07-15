for _ in range(int(input())):
 n = int(input())
 arr = list(map(int,input().split()))

 d = {}

 i = 0

 flag = True
 while i<n:
  if arr[i] not in d:
   
   count = 1

   while i<n-1 and arr[i]==arr[i+1]:
    count+=1
    i+=1
   
   d[arr[i]] = count

  else:
   flag = False
   break

  i+=1
 
 # print(d,flag)

 if flag==False:
  print("NO")
 else:
  t = list(d.values())

  if len(t)==len(set(t)):
   print("YES")
  else:
   print("NO")

  

  
  


 



 

