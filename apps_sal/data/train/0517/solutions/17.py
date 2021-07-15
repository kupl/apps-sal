from math import sqrt, gcd
n, MOD = list(map(int, input().split()))
factors = set()
for i in range(2, 1+int(sqrt(n))):
    if(n % i == 0):
        factors.add(i)
        factors.add(n//i)
factors = sorted(list(factors), reverse = True)
ans = 2**n
if(factors == []):
    ans -= 2
done = []
for i in factors:
    ans -= (2**i) % MOD
    temp = i
    #print("i=",i,ans)
    for j in done:
        if(temp == 1):
            break
        ans = (ans + (2**gcd(temp,j))%MOD) % MOD
        temp //= gcd(temp,j)
        #print("j=",j,ans)
    done.append(i)
if(factors):
    ans -= max(0,len(factors)//2 - 1) * 2
print(ans%MOD)
