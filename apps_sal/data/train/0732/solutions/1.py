for _ in range(int(input())):
 n = int(input())

 arr1 = list(map(int,input().split()))
 arr2 = list(map(int,input().split()))
 res=0
 presum1=0
 presum2=0
 for i in range(n):
  if arr1[i]== arr2[i] and presum1==presum2 :
   
   res+=arr1[i]
  presum1+=arr1[i]
  presum2 +=arr2[i]
  
 print(res)

   



 




 



