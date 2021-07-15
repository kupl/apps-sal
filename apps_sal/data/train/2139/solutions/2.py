import sys
input = sys.stdin.readline
mod=998244353
n=int(input())
a=list(map(int,input().split()))
a.sort()
val=0
for i in range(n):
    val+=a[-i-1]
    val-=a[i]
facs=[1]
for i in range(2*n):
    facs.append((facs[-1]*(i+1))%mod)
numb=facs[2*n]
numb*=pow(facs[n]**2,mod-2,mod)
numb*=val
numb%=mod
print(numb)
