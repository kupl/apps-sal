# cook your dish here
for i in range(int(input())):
 a,b=list(map(int,input().split()))
 limak,bob=0,0
 winner=''
 i=1
 while(i<10000):
  if i%2!=0:
   limak+=i
   if limak>a:
    winner='Bob'
    break
  else:
   bob+=i
   if bob>b:
    winner='Limak'
    break
  i+=1
 print(winner)

