# cook your dish here
for T in range(int(input())):
 s,n = list(map(int,input().split()))
 coins = 0
 
 if (s%2!=0):
  s -=1 
  coins += 1 
 
 coins += (s//n)
 if(s%n!=0):
  coins += 1 
 
 print(coins)
   
  

