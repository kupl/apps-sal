a=[]
mod=1000000007
a.append([])
a[0].append(0)
a[0].append(1)
a.append([])
a[1].append(2)
a[1].append(1)
a.append([])
a[2].append(3)
a[2].append(2)
for i in range(3,100001):
 a.append([])
 a[i].append((a[i-1][0]+a[i-2][0]+a[i-3][0])%mod)
 a[i].append((a[i-1][1]+a[i-2][1]+a[i-3][1])%mod)
t=eval(input())
while t:
 n=eval(input())
 print(a[n-1][0]%mod,a[n-1][1]%mod)
 t-=1

