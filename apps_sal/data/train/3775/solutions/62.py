def digits(n):
   if n==0:
       return 1
   ans = 0
   while n!=0:
       n  =  n//10
       ans += 1
   return ans
