t = int(input())
for _ in range(t):
 num = int(input())
 if num%5 != 0:
  print(-1)
  continue
 count = 0
 while True:
  if num%10 == 0:
   break
  num*=2
  count+=1
 print(count)
