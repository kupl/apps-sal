T=int(input())
a=[]
a.append(1)
for j in range(10**5+1):
 a.append(a[j]*(j+1)%1589540031)
for i in range(T):
 N=int(input())
 print(a[N])
