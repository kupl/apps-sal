MOD = 10**9+7

fact = [1]*200003
for i in range(1,200003):
    fact[i] = (fact[i-1]*i)%MOD
inv = [1]*200003
for i in range(2,200003):
    inv[i] = (-(MOD//i)*inv[MOD%i])%MOD
for i in range(2,200003):
    inv[i] = (inv[i]*inv[i-1])%MOD
def C(n,k):
    return (fact[n]*inv[k]*inv[n-k])%MOD
h,w,n = map(int,input().split(" "))
mas=[]
for i in range(n):
    x,y= map(int,input().split(" "))
    mas.append([x,y,0,0])
mas.append([h,w,0,0])
mas.sort(key=lambda x: x[0]+x[1])

for j in mas:
    j[2] = C(j[0]+j[1]-2,j[0]-1)%MOD
    for i in mas:
        if (j[0]==i[0] and j[1]==i[1]): break
        if i[0]<=j[0] and i[1]<=j[1]:
            l=C(j[0]-i[0]+j[1]-i[1],j[0]-i[0])%MOD
            k= i[2]
            j[2]-=l*k%MOD



print(mas[-1][2]%MOD)
