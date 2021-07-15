for _ in range(int(input())):
 n,origin=map(str,input().split())
 sum=0
 for i in range(int(n)):
  arr=list(map(str,input().split()))
  kind=arr[0]
  if(kind=="CONTEST_WON"):
   rank=int(arr[1])
   bons=max(0,20-rank)
   sum+=(300+bons)
  elif(arr[0]=="TOP_CONTRIBUTOR"):
   sum+=300
  elif(arr[0]=="BUG_FOUND"):
   sum+=int(arr[1])
  else:
   sum+=50
 if(origin=="INDIAN"):
  print(sum//200)
 else:
  print(sum//400)
