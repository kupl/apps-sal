t = eval(input())
t = int(t)
c =1000000007
for each in range(t):
 n = eval(input())
 n = int(n)
 n2 = n
 result = 1
 base = 3
 while(n>0): 
  if(n%2==1): 
   result = (result*base)%c
  n = n>>1
  base = (base*base)%c
 if(n2%2==0):
  result = result+3
 else:
  result = result-3
 print(str(result))

