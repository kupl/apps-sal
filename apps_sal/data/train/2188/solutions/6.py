t=int(input())
T=str.maketrans('0123456789','0101010101')
d={}
for _ in ' '*t:
    a,b=input().split()
    b=int(b.translate(T))
    if a=='?':print(d.get(b,0))
    elif a=='+':d[b]=d.get(b,0)+1
    else:d[b]-=1
