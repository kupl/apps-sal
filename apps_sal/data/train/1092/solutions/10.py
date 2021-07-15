# cook your dish here

for _ in range(int(input())):
 n,k,e,m=map(int,input().strip().split())
 res_arr=[]
 
 for i in range(n-1):
  res_arr.append(sum(map(int,input().strip().split())))
  
 res_arr=sorted(res_arr,reverse=True)[:k]
 serg_mrks=sum(map(int,input().strip().split()))
 
 least_max=res_arr[k-1]
 if(least_max<m*e):
  if(least_max>=serg_mrks):
   finl_mrks=least_max-serg_mrks+1
   print(finl_mrks if finl_mrks<=m else 'Impossible')
  else:
   print(0)
 else:
  print('Impossible')
