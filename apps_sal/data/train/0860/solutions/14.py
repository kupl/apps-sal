# cook your dish here
def MinimumHours(n,h,a):
 a.sort()
 j=0
 mi=0
 s=0
 c=0
 while 1:
  mi+=1
  for i in a[-1:-(n+1):-1]:
   if i%mi==0:
    s+=(i//mi)
   else:
    s+=(i//mi)+1
   if s>h:
    c=1
    break
  if c==1:
   c=0
   s=0
  else:
   return mi
 
 
p=[]
for i in range(int(input())):
 n,h=input().split()
 p.append(MinimumHours(int(n),int(h),[int(i) for i in input().split()]))
 
for i in p:
 print(i)

