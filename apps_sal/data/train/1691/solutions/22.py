import sys
n,m,c=list(map(int,input().split()))

k=1
li=[]
query=m/n
rem=0
if c<=query:
       query=c
       rem=m-query*n

for i in range(query):
       print(2,1,n,k,k+n-1)
       sys.stdout.flush()
       sum=int(input())
       li.append(str(sum/(n*n)))
       #print m,k
       if k>=m:break
       k+=n
print(3)
       
for i in range(n):
       for j in range(query):
              print(" ".join([li[j]]*n), end=' ')
       print(" ".join(["25"]*rem))

       


       

       

