a=[]
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
 a[i].append((a[i-1][0]+a[i-2][0]+a[i-3][0])%1000000007)
 a[i].append((a[i-1][1]+a[i-2][1]+a[i-3][1])%1000000007)
t=eval(input())
while t:
 n=eval(input())
 print(a[n-1][0],a[n-1][1])
 t-=1

