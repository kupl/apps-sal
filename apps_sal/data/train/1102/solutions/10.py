M = 1000000007
def letterCombinations(s):
 n = len(s)
 digits = list(s)
 if n==0:
  return []
 table = [0,0,3,3,3,3,3,4,3,4]
 
 ans = 1
 for i in range(n):
  ans = (ans* table[int(digits[i])])%M
 print(ans%M)

t = int(input())
while t>0:
 s = input().strip()
 letterCombinations(s)
 
 t-=1
