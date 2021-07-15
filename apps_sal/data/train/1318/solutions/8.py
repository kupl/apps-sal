# cook your dish here
for _ in range(int(input())):
 n,k=list(map(int,input().split()))
 sum=0
 #This denotes the max triangle of K length possible in base  
 maxi=n-k+1
 if k>n:
  sum=0
 else:
  for i in range(1,n+1):
   sum+=i
   if i==maxi:
    break
 print('Case'+' '+str(_+1)+':',sum)

