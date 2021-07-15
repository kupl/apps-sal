t=int(input())
for i in range(t):
 n=int(input())
 final=0
 winner=-1
 winnerPoints=[0]*(n+1)
 for j in range(n):
  c=[int(num) for num in input().strip().split()]
  arr=[0]*6
  for k in range(1,c[0]+1):
   arr[c[k]-1]+=1
  arr.sort()
  six=arr[0]
  five=arr[1]-six
  four=arr[2]-five
  point=(six*4)+(five*2)+(four*1)+c[0]
  if(point>final):
   final=point
   winner=j+1
  winnerPoints[j+1]=point
 count=0
 for t in range(1,n+1):
  if(winnerPoints[t]==final):
   count+=1
 if(count>1):
  print("tie")
 elif(winner==1):
  print("chef")
 else:
  print(str(winner))
