R=[0,0]

s=0
p=0
S={0}
for i in range(1,2500000):
    x=p-i
    if x<0 or x in S:x=p+i
    S|={x}
    s+=x
    p=x
    R+=[s]
def rec(x):return R[x]
