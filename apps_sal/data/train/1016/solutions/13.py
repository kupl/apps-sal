# cook your dish here
for _ in range(int(input())):
 c=0
 for __ in range(int(input())):
  a,b=map(int,(input().split()))
  if((b-a)>5):
   c+=1
 print(c)
