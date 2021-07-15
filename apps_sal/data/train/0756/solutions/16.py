# cook your dish here
def check_prime(num):
 for i in range(2,num):

  if num%i==0:
   return ('Not Prime')

 else:
  return ('Prime')

t=int(input())
for i in range(t):
 n,m=list(map(int,input().split()))
 s=n+m
 if s%2==0:
  s+=1
  while check_prime(s)!='Prime':
   s+=2
   res= check_prime(s)
   if res=='Prime':
    print(s-n-m)
    break
  else:
   print(s-n-m)
 else:

  while True :
   s += 2
   res = check_prime(s)
   if res == 'Prime':
    print(s-n-m)
    break


