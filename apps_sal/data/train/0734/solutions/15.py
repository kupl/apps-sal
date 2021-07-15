for test in range(int(input())):
 n=int(input())
 arr=list(map(int,input().split()))
 mp=[]
 for i in range(n):
  mp.append([arr[i],i])
 mp.sort(key=lambda x:x[0])
 prev=-1
 max=-1
 count=1
 for i in range(n):
  if prev==mp[i][0]:
   count+=1
  else:
   count=1
  if count>max:
   max=count
  prev=mp[i][0]
 if 2*max>n:
  print("No")
 else:
  print("Yes")
  x=[0]*n
  for i in range(n):
   x[(i+max)%n]=mp[i][0]
  y=[0]*n
  for i in range(n):
   y[mp[i][1]]=x[i]
  for i in range(n):
   print(y[i],end=' ')
  print()

