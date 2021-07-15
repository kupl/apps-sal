n= int(input())
for i in range(n):
   a= int(input())
   s=0
   while a!=0:
       s+=a%10
       a=int(a/10)
   print(s)
