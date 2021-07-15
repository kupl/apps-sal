import math
# Source Stack Overflow :p
def divisorGenerator(n):
 large_divisors = []
 for i in range(1, int(math.sqrt(n) + 1)):
  if n % i == 0:
   yield i
   if i*i != n:
    large_divisors.append(n / i)
 for divisor in reversed(large_divisors):
  yield divisor

 
 
 #return len(k)
for KK_KK in range(eval(input())):

 a=eval(input())
 k= list(divisorGenerator(a))
 #print k
 if len(k)%2==0:
  print("NO")
 else:
  print("YES")

