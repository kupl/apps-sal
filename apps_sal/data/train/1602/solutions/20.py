t = int(input())
lis = []
for i in range(t):

 n = int(input())
 x = int(input())
 expiry = [int(i) for i in input().split()]
 day = 1
 val = x

 expiry.sort()

 while(n > 0):

  if expiry[0] > day:
   expiry.pop(0)
   n = n-1
   val = val-1
  else:
   lis.append("Impossible")
   break
  if(val == 0):
   day += 1
   val = x
 if(n == 0):
  lis.append("Possible")
'''
     for i in range(x):
      if expiry[i]>day:
       expiry.pop(0)
       n = n-1
       if n==0:
        lis.append("Possible")
        break
        #val = False
      else:
       lis.append("Impossible")
       break
       #val = False
     day+=1
'''
for i in lis:
 print(i)

