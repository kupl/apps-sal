from functools import reduce
def get_prime_factors(number):
 if number == 1:
  return []

 for i in range(2, number):
  # Get remainder and quotient
  rd, qt = divmod(number, i)
  if not qt: # if equal to zero
   return [i] + get_prime_factors(rd)

 return [number]

T = int(input())

for j in range(T):
 n = int(input())
 divisors = get_prime_factors(n)
 #print divisors
 
 count = [1 for x in range(len(divisors))] 
 for i in range(len(divisors)):
  while n%divisors[i] == 0:
   count[i]=count[i]+1
   n=n/divisors[i]
   
 # print count
 num = reduce(lambda x, y: x*y, count)

 if num%2==0:
  print("NO")
 else:
  print("YES")
 

