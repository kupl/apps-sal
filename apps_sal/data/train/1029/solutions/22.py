for _ in range(int(input())):
 [n,m] = [int(i) for i in input().split()]
 l = sorted([int(i) for i in input().split()])
 tempI = 1
 aI = 0
 temp = []
 while(tempI <= n):    
  if (aI < m) and (tempI == l[aI]):
   aI += 1
   tempI += 1
   continue
  temp.append(tempI)
  tempI += 1
 #print(temp)
 if(n-m) <= 0:
  print()
  print()
  continue
 if(n - m) == 1 :
  print(temp[0])
  print()
  continue
 for i in range(0,n - m, 2):
  print(temp[i], end = " ")
 print()
 for i in range(1, n - m, 2):
  print(temp[i],end = " ")
 print()
