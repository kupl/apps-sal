# cook your dish here
n,k=list(map(int,input().split()))
j=list(map(int,input().split()))
j.sort()
c=0;r=0;
#print(j)
l=len(j)
for i in range(0,l):
 if(j[i]<k) and ((k-r)>j[i]):
  r=r+j[i]
  c=c+1
  #print(j[i])
print(c)
