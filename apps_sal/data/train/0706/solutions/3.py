for _ in range(int(input())):
 n,k = list(map(int,input().split()))
 arr = list(map(int,input().split()))

 count = 0

 flag = True
 curr_sum = 0
 for i in arr:
  if i>k:
   flag = False
  else:
   curr_sum+=i

   if curr_sum>k:
    curr_sum = i
    count+=1
 

 if curr_sum<=k:
  count+=1
 if flag==False:
  print(-1)
 else:
  print(count)

 
 

