for _ in range(int(input())):
 n = int(input())
 a = list(map(int,input().split()))
 fmax=smax=count= 0
 for i in range(n):
  if a[i]==1:
   if count!=0:
    if count>fmax:
     smax = fmax 
     fmax = count
    elif count>smax:
     smax = count
    count = 0 
  else:
   count+=1
 if (fmax%2!=0 and smax<(fmax+1)//2):
  print("Yes")
 else:
  print("No")

