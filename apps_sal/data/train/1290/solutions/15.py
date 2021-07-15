# cook your dish here
try:
 n = int(input())
 i = 0
 while(n>=10**i):
  i = i+1
 if(i<=3):
  print(i)
 else:
  print("More than 3 digits")
except:
 pass
