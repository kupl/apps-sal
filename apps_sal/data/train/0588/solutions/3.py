# cook your dish here
def isDivisible(a, k):
 for i in a:
  if (i%k!=0):
   return False
 return True
def find_gcd(x, y): 
  
 while(y): 
  x, y = y, x % y 
  
 return x 
   
def findHCF(l):
 gcd = find_gcd(l[0], l[1]) 
  
 for i in range(2, len(l)): 
  gcd = find_gcd(gcd, l[i]) 
 return gcd
def calDegree(a):
 b = []
 p = a[0]
 i = 1
 while(i<len(a)):
  b.append((a[i]-p)%360)
  p = a[i]
  i+=1
 return b
def calRawCount(a, k):
 s = 0
 for i in a:
  s+=(i//k)
 return s
t = int(input())
for _ in range(t):
 n = int(input())
 l = list(map(int, input().split(" ")))
 l.append(l[0])
 a = calDegree(l)
 
 HCF = findHCF(a)
 
 raw_count = calRawCount(a, HCF)
 print(raw_count-len(l)+1)

