T=int(input())
for i in range(0,T):
 N=int(input())
 b=[int(x) for x in input().split()]
 p=[float(x) for x in input().split()]
 arr=[0]*32
 for j in range(0,len(b)):
  st=bin(b[j])
  st=st[2:]
  #print(st)
  for k in range(1,len(st)+1):
   if(st[-k]=='1'):
    arr[k-1]=((1-arr[k-1])*p[j])+((1-p[j])*arr[k-1])
  #for k in range(len(st)-1,-1,-1):
   #if(st[k]=='1'):
    #arr[N-k-1]=(arr[N-k-1]*(1-p[j]))+((1-arr[N-k-1])*p[j])
    #print(N-k,arr)
 #print(arr)

 exp=0
 xr=1
 for j in range(0,len(arr)):
  exp=exp+(xr*arr[j])
  xr=xr*2

 print(exp)



