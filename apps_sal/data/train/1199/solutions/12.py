for _ in range(int(input())):
 s,n = list(map(int,input().split()))
 biggest = (n//2)*2
 coins,balance = divmod(s,biggest)
 if balance == 0 :
  print(coins)
 elif balance == 1 or balance%2==0:
  print(coins+1)
 else :
  print(coins+2)

