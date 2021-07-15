import sys,random
n,m,c=list(map(int,input().split()))
print(2,1,n,1,m)
sys.stdout.flush()
sum=int(input())
sum/=(n*m)
print(3)
sys.stdout.flush()
if sum-5<1:
       l=0
       r=sum+5
else:
       l=sum-5
       r=sum+5
for i in range(n):
       for j in range(m-1):
                     print(random.randrange(l,r), end=' ')
       print(random.randrange(l,r))

