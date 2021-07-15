def fun(lst, k):
 
 weight = 0
 ans = 1
 
 for el in lst:
  
  if el > k:
   return -1
  
  elif weight + el <= k:
   weight += el
   
  else:
   ans += 1
   weight = el
 return ans


for _ in range(int(input())):
 
 n, k = list(map(int, input().split()))
 lst = [int(i) for i in input().split()]
 
 print(fun(lst, k))

