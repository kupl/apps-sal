def primes(n):
 nums = [True for i in range(n+1)] 
 lst = []
 p = 2
 while (p * p <= n): 
  if (nums[p] == True): 
   for i in range(p * p, n+1, p): 
    nums[i] = False
  p += 1
 for p in range(2, n+1): 
  if nums[p]: 
   lst.append(p)
 return lst
for _ in range(int(input())):
 n = int(input())
 lst = primes(n)
 print(sum(lst))

