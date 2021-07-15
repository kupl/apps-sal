# cook your dish here
from collections import defaultdict
from math import sqrt

"""def isprime(n):
    if n==2:
        return True
    elif n>2:
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                return False
    elif n<2:
        return False
    return True"""

def primefact(n):
    pf = []
    if n%2==0:
        pf.append(2)
        while n%2==0:
            n //= 2
    for i in range(3,int(sqrt(n))+1):
        if n%i==0:
            while n%i==0:
                n //= i
            pf.append(i)
    if n>2:
        pf.append(int(n))
    return pf
    
K,Q = map(int, input().split())
prime_range = {}
pfk = primefact(K)
for i in range(Q):
    query = input().split()
    if query[0]=="!":
        l = int(query[1])
        r = int(query[2])
        start = l
        end = r
        for i in sorted(prime_range):
            if start>i[1]:
                continue
            if end<i[0]:
                break
            startrange = start
            endrange = end
            if start>=i[0] and start<=i[1]:
                start = i[1]+1
                continue
            if end>=i[0]:
                endrange = i[0]-1
            if (startrange<=endrange):
                prime_range[(startrange,endrange)] = int(query[3])
                start = max(endrange+1,i[1]+1)
        if start<=end:
            prime_range[(start,end)] = int(query[3])
    else:
        l = int(query[1])
        r = int(query[2])
        res = []
        count = 0
        for primenum in pfk:
            for currRange in prime_range:
                if (not (r < currRange[0] or l > currRange[1])) :
                    num = prime_range[currRange]
                    if (num % primenum == 0) :
                        count += 1
                        break
        res.append(count)
        for r in res:
            print(r)
        '''for i in prime_range:
            if l>=i[0] and l<=i[1]:
                x = prime_range[(i[0],i[1])]
                pf = primefact(x)
                for p in pf:
                    if p in pfk and p not in pfc:
                        pfc.append(p)
                continue
            if r>=i[0] and r<=i[1]:
                x = prime_range[(i[0],i[1])]
                pf = primefact(x)
                for p in pf:
                    if p in pfk and p not in pfc:
                        pfc.append(p)
        print(len(pfc))
       #print(prime_range)'''
                
            
        
