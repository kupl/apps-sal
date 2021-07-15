test_case = int(input())
while test_case :
 n = int(input())
 xdict = {}
 ydict = {}
 total_points = 4*n-1
 for _ in range(total_points) :
  x,y = map(int, input().split())
  if x not in xdict :
   xdict[x] = 1 
  else:
   xdict[x] += 1 
  
  if y not in ydict :
   ydict[y] = 1 
  else:
   ydict[y] += 1 
 
 for key in xdict.keys() :
  if xdict[key] % 2 != 0 :
   print(key, end = ' ')
   break
 for key in ydict.keys():
  if ydict[key] % 2 != 0 :
   print(key)
   break
 
 test_case -= 1
 
 
 
 
 
 
 
 
 
 
 
