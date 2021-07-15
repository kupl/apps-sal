# cook your dish here
for u in range(int(input())):
 n = int(input())
 gas = list(map(int, input().split()))[:n]
 dist1 = 0
 dist = 0
 for i in gas:
  if i == 0 and dist == 0:
   break
  else:
   dist = dist+i
   dist -= 1
  dist1 += 1
 print(dist+dist1)
