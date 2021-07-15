# cook your dish here
T=int(input())
while T:
 N=int(input())
 s=str(input())
 l=list(map(int,input().split()))
 
 re=[]
 for i in range(N-7):
  sum=0
  d1=1
  t1=1
  for j in range(len(l)):
   if s[i+j]==".":
    sum=sum+l[j]
   elif s[i+j]=="d":
    sum=sum+l[j]*2
   elif s[i+j]=="t":
    sum=sum+l[j]*3
   elif s[i+j]=="D":
    sum=sum+l[j]
    d1=d1*2
   elif s[i+j]=="T":
    sum=sum+l[j]
    t1=t1*3
 
  if d1>1 and t1>1:
   sum=sum*d1*t1
  elif d1>1:
   sum=sum*d1
  else:
   sum=sum*t1
  re.append(sum)
  
 print(max(re))
 T=T-1

