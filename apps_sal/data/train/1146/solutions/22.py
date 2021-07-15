# cook your dish here
n,d=map(int,input().split())
l=[]
for i in range(0,n):
 l.append(int(input()))
l.sort()
c=0
i=0
while i<n-1:
 if abs(l[i]-l[i+1])<=d:
  c=c+1
  i=i+2
 else :
  i=i+1
print(c)
