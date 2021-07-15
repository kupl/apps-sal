# cook your dish here
def solve():
 t = int(input())
 for i in range(0, t):
  s = input()
  
  ans = 0
  
  sums = 0
  
  for k in range(0,len(s)-1):
   if s[k] == s[k+1]:
    sums += 1
  
  ans = len(s)*(len(s)+1)/2*sums
  
  for l in range(0, len(s)):
   for r in range(l, len(s)):
    if l>0:
     if s[l-1] == s[l]:
      ans -= 1
     else:
      ans += 1
    if r<len(s)-1:
     if s[r] == s[r+1]:
      ans -= 1
     else:
      ans += 1
  print(int(ans))
  
solve()
