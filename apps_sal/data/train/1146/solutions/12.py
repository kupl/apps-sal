# cook your dish here
# cook your dish here
n,d=map(int,input().split())
l=[]
for i in range(n):
 l.append(int(input()))
l.sort()
count=0
i=n-1
while i>0:
 if l[i]-l[i-1]<=d:
  count+=1
  i-=2
 else:
  i-=1
print(count)
