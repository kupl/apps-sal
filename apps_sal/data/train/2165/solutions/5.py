MOD = 10**9+7



fact = [1]*200013
for i in range(1,200013):
    fact[i] = (fact[i-1]*i)%MOD
inv = [1]*200013

for i in range(2,200013):
    inv[i] = pow(fact[i],MOD-2,MOD)
def C(n,k):
    return (fact[n]*inv[k]*inv[n-k])%MOD

def rasch(x,y):

    nonlocal mas
    res = C(x+y-2,x-1)%MOD
    for i in mas:
        if (x==i[0] and y==i[1]): break
        if i[0]<=x and i[1]<=y  :
            l=C(x-i[0]+y-i[1],x-i[0])
            k=rasch(i[0],i[1]) if not i[3] else i[2]
            i[2]=k%MOD
            i[3]=1
            res-=l*k%MOD
    return res%MOD
h,w,n = map(int,input().split(" "))
mas=[]
for i in range(n):
    x,y= map(int,input().split(" "))
    mas.append([x,y,0,0])
mas.sort(key=lambda x: x[0]+x[1])
print(rasch(h,w)%MOD)
