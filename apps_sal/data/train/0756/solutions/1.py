# cook your dish here
t = int(input())
def isPrime(num):
 c = 0
 for i in range(2,num):
  if num % i == 0:
   c = c + 1 
 if c == 0:
  return 0
 else:
  return 1
for i in range(t):
 a,b = list(map(int,input().split()))
 i = 1
 res = 0
 while(isPrime(a+b+i)):
  res = res + 1
  i = i + 1
 print(res + 1)
  

