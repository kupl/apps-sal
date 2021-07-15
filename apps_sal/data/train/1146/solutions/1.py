# cook your dish here

a,b=list(map(int,input().split()))
ls=[]
for i in range(a):
 ls.append(int(input()))
ls.sort()
c=0;i=0
while i<(a-1):
 if ls[i+1]-ls[i]<=b:
  c=c+1
  i=i+1
 i=i+1
print(c)

