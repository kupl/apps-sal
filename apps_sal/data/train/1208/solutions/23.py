from sys import stdin,stdout
a=[0]*(10**6 + 1)
mod=10**9 + 7
a[1]=1
p=1
for i in range(2,10**6 + 1):
 a[i]=(a[i-1]*((p*i)%mod)%mod)
 p*=i
 p=p%mod
t=int(stdin.readline())
for i in range(t):
 n=int(stdin.readline())
 stdout.write(str(a[n]))
 stdout.write('\n')
