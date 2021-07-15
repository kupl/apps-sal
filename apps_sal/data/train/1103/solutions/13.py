import math

def divisorGenerator(n):
 large_divisors = []
 for i in range(2, int(math.sqrt(n) + 1)):
  if n % i == 0:
   yield i
   if i*i != n:
    large_divisors.append(n / i)
 for divisor in reversed(large_divisors):
  yield divisor
t = int(input())
while t>0 :
 n = int(input())
 a = list(map(int,input().split()))
 p = 1
 for i in a:
  p = p * i
 s = list(divisorGenerator(p))

 for j in s:
  if p % (j**2) ==0 :
   print(j)
   break
 t = t - 1 

