t = int(input())

for x in range(0, t):
 s, n = list(map(int, input().split()))

 coin = 0

 if(s > n):
  rem = s%n
  coin += int(s/n)

  if(rem%2 == 0 and rem != 0):
   print(coin + 1)
  elif(rem == 0):
   print(coin)
  elif(rem == 1):
   print(coin + 1)
  elif(rem%2 >= 1):
   print(coin + 2)

 elif(s <= n):        
  if(s%2 == 0):
   print(coin + 1)
  elif(s == 1):
   print(coin + 1)
  elif(s%2 >= 1 and s != 1):
   print(coin + 2)
 


