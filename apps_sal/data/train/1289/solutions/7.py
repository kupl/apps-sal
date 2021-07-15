N=eval(input())
n=int(N)
a=[]
while n>0:
 a.append(eval(input()))
 n=n-1
i=0
for value in a:
 a[i]=int(value)
 i=i+1
b=[1,3]
i=2
k=5
while i<100:
 b.append(b[i-1]*k)
 k=k+2
 i=i+1
i=0
n=int(N)
while n>0:
 print(b[a[i]-1])
 i=i+1
 n=n-1

