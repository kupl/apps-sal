from sys import stdin
import functools
def gcd(a, b):  
 if (a == 0): 
  return b 
 return gcd(b % a, a) 
 
# Recursive function to calculate the  
# number of subsequences with gcd 1  
# starting with particular index  
MAX=10001
def func(ind, g, dp, n, a): 
 
 # Base case  
 if (ind == n):  
  if (g == 1):  
   return 1
  else: 
   return 0
 
 # If already visited  
 if (dp[ind][g] != -1):  
  return dp[ind][g] 
 
 # Either we take or we do not  
 ans = (func(ind + 1, g, dp, n, a) + 
   func(ind + 1, gcd(a[ind], g),  
        dp, n, a)) 
 
 # Return the answer  
 dp[ind][g] = ans 
 return dp[ind][g] 
 
# Function to return the number  
# of subsequences  
def countSubsequences(a, n):  
 
 # Hash table to memoize  
 dp = [[-1 for i in range(MAX)] 
    for i in range(n)] 
 
 # Count the number of subsequences  
 count = 0
 
 # Count for every subsequence  
 for i in range(n):  
  count += func(i + 1, a[i], dp, n, a) 
 
 return count 
tc=int(stdin.readline())
for i in range(tc):
 n=int(stdin.readline())
 list1=list(map(int,stdin.readline().split()))
 print(countSubsequences(list1,n))


