import math

for _i in range(int(input())):
 n = int(input())
 arr = list(map(int,input().split()))
 arr.sort()
 grams,flav = list(map(int,input().split()))
 cost = 0
 if(grams<flav):
  print("Not Possible")
  continue
 elif(grams==flav):
  cost = sum(arr[0:flav])
 else:
  cost = cost + (grams-flav+1)*arr[0]
  cost = cost+sum(arr[1:flav])
 print(cost)


 




