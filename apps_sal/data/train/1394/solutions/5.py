import math as m
mod = 1000000007
for t in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(1,m.floor(m.sqrt(n))+1):
     ans += i*((m.floor(n/i) * ((m.floor(n/i)+1))-(i*(i-1))))
     ans -= (i*i)
    print(ans%mod)
