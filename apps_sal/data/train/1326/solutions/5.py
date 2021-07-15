for _ in range(int(input())):
 n = int(input())
 arr = list(map(int,input().split()))
 dis = 0
 fuel = arr[0]
 for i in range(1,n):
  if fuel > 0:
   fuel -= 1
   dis += 1
   fuel += arr[i]
  else:
   break
 
 dis += fuel
 print(dis)

