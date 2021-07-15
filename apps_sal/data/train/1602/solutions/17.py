# cook your dish here
t=int(input())
for y in range(t):
 flag=True
 n=int(input())
 x=int(input())
 arr=list(map(int,input().split()))
 arr.sort(reverse=True)
 while(len(arr)!=0):
  for k in range(len(arr)):
   arr[k]=arr[k]-1
   if(arr[k]==0):
    flag=False
    break
  for j in range(x):
   try:
    arr.pop()
   except :
    pass
 if(flag==True):
  print('Possible')
 else:
  print('Impossible')

