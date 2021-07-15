def exp(a,p,m):
    ans = 1
    while(p!=0):
        if(p%2==1):
            ans*=a
            ans%=mod
        a*=a
        a%=mod
        p>>=1
    return ans
mod = (10**9)+7
fact = [1]
for i in range(1,1+(10**5)):
    x = fact[-1]
    x = (x*i)%mod
    fact += [x]
inv_fact = []
for i in fact:
    x = exp(i,mod-2,mod)
    inv_fact += [x]
t = eval(input())
for _ in range(t):
    s = input()
    hs = [0]*26
    for i in s:
        x = ord(i) - 97
        hs[x]+=1
    l = len(s)
    tot_num = fact[l]
    for i in hs:
        tot_num *= inv_fact[i]
        tot_num %= mod
    xy = 1
    for i in range(26):
        for j in range(i+1,26):
            xy += (hs[i]*hs[j])
            xy %= mod
    for i in range(26):
        for j in range(i+1,26):
            for k in range(j+1,26):
                xy += (hs[i]*hs[j]*hs[k]*2)
                xy %= mod
    for i in range(26):
        for j in range(i+1,26):
            x = (hs[i]*(hs[i]-1))/2
            x %= mod
            y = (hs[j]*(hs[j]-1))/2
            y %= mod
            x*=y
            x%=mod
            xy+=x
            xy%=mod
    for i in range(26):
        for j in range(26):
            for k in range(j+1,26):
                if(i!=j and i!=k):
                    x = hs[i]*(hs[i]-1)
                    x%=mod
                    x*=hs[j]
                    x%=mod
                    x*=hs[k]
                    x%=mod
                    xy+=x
                    xy%=mod
    for a in range(26):
        for b in range(a+1,26):
            for c in range(b+1,26):
                for d in range(c+1,26):
                    x = (hs[a]*hs[b])%mod
                    x *= hs[c]
                    x %= mod
                    x *= hs[d]
                    x%=mod
                    x*=3
                    x%=mod
                    xy+=x
                    xy%=mod
    t1 = (tot_num*tot_num)%mod
    t2 = (tot_num *xy)%mod
    t1-=t2
    while(t1<0):
        t1+=mod
    print(t1)

