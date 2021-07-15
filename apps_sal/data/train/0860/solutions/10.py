# cook your dish here
def MinimumHours(n,h,a):
 a.sort()
 b=a[0]
 c=0
 s=0
 j=0
 m=1
 while 1:
  for i in a[-1:-(n+2):-1]:
   if i%m==0:
    s+=i//m
   else:
    s+=(i//m)+1
   if s>h:
    break
  if s<=h:
   return m
  m+=1
  s=0
   
  
 
p=[]
for i in range(int(input())):
 n,h=input().split()
 p.append(MinimumHours(int(n),int(h),[int(i) for i in input().split()]))
 
for i in p:
 print(i)

