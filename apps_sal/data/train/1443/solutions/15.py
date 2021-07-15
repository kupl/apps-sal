def comb(n, r):
 an = fact(n)
 an = an/fact(r)
 an = an/fact(n-r)
 
 return int(an)
 
def fact(n):
 ans = 1
 while(n>1):
  ans = ans*n
  n -= 1
 return ans
 
t = int(input())

for _ in range(t):
 n, m = [int(x) for x in input().split()]
 
 a = []
 ans = 0
 
 for i in range(n):
  temp = [int(x) for x in input()]
  a.append(temp)
 
 for i in range(m):
  c = 0
  for j in range(n):
   if(a[j][i] == 1):
    c += 1
  if(c>=2):
   ans += comb(c, 2)
 
 print(ans)
