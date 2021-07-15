n= int(input())
co =[]
hi=[]
for i in range(n):
 arr=[int(x) for x in input().split()]
 co.append(arr[0])
 hi.append(arr[-1])
 
if n<=2:
 count=n
else:
 count=2
 for i in range(1,n-1):
  if hi[i]<co[i]-co[i-1]:
   count+=1
  elif hi[i]<co[i+1]-co[i]:
   count+=1
   co[i]+=hi[i]
  else:
   continue
print(count)
