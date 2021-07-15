# cook your dish here
for _ in range(int(input())):
 S,N=(int(i) for i in input().strip().split())
 coinCount=0
 if(S%2==1):
  S-=1
  coinCount+=1
 coinCount+=S//N
 if(S%N!=0):
  coinCount+=1
 print(coinCount)
