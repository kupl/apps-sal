# cook your dish here
for _ in range(int(input())):
 a,b=map(int,input().split())
 i=1
 limak=bob=0
 while True:
  limak+=i
  bob+=i+1
  i+=2
  if limak>a:
   print('Bob')
   break
  elif bob>b:
   print('Limak')
   break
