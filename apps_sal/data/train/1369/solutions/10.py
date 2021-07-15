# cook your dish here
def sieve(n):
 prime = [True for i in range(n+1)]
 p = 2
 while (p * p <= n):
  if (prime[p] == True):
   for i in range(p * p, n+1, p):
    prime[i] = False
  p += 1
 return prime
for u in range(int(input())):
 n=int(input())
 l=sieve(n)
 s=0
 for i in range(2,n+1):
  if(l[i]==True):
   s=s+i
 print(s)

