# cook your dish here
for x in range(int(input())):
 l,r=list(map(int,input().split()))
 c=0
 if l-r<=0:
  for y in range(l,r+1):
   if y%10 in [2,3,9]:
    c+=1
 else:
  c=3*(r//10-l//10)
  for y in range(l%10):
   if y in [2,3,9]:
    c-=1
  for y in range(r%10):
   if y in [2,3,9]:
    c+=1
 print(c)
   

