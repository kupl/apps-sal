n=int(input())
d={}
D={}
for i in range(n):
    h,*p=(input()[7:]+'/').split('/')
    d.setdefault(h,set()).add('/'.join(p))
for x in d: D.setdefault(frozenset(d[x]),[]).append(x)

def ans():
    for x in D:
        if len(D[x])>1:
            yield 'http://'+' http://'.join(D[x])

print(sum(1 for x in D if len(D[x])>1))
print('\n'.join(ans()))
