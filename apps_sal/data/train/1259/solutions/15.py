t = int(input())
while t>0:
 l,r = tuple([int(i) for i in input().split()])
 c = 0
 for i in range(l,r+1):
  num = list(str(i))[-1]
  if '2' == num or '3' == num or '9' == num:
   #print(i)
   c+=1
 print(c)
 t-=1


