for _ in range(int(input())):
 n = int(input())
 # h,p = map(int,input().split())
 net = 0
 tax = 0
 if n<=250000 :
  print(int(n))
 elif n<=500000 :
  tax = (n-250000)*0.05
  print(int(n-tax))
 elif n<=750000 :
  tax = 12500 + (n-500000)*0.10
  print(int(n-tax))
 elif n<=1000000 :
  tax = 12500 + 25000 + (n-750000)*0.15
  print(int(n-tax))
 elif n<=1250000 :
  tax = 12500 + 25000 + 37500 + (n-1000000)*0.20
  print(int(n-tax))
 elif n<=1500000 :
  tax = 12500 + 25000 + 37500 + 50000 + (n-1250000)*0.25
  print(int(n-tax))
 else :
  tax = 12500 + 25000 + 37500 + 50000 + 62500 + (n-1500000)*0.30
  print(int(n-tax))

