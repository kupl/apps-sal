# cook your dish here
for i in range(int(input())):
  x,p = map(int,input().split())
  l=list(map(int,input().split()))
  a=b=0
  for j in l:
   if j >= int(p/2):
    a +=1 
   elif j <= int(p/10):
    b += 1
  print('yes' if(a==1 and b==2) else 'no') 
