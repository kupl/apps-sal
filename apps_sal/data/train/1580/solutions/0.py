import sys
t=int(input())
x=sys.stdin.readlines()
l=[]
for s in x:
    s=s.replace(".","")
    s=s.replace("'","")
    s=s.replace(",","")
    s=s.replace(":","")
    s=s.replace(";","")
    lst=[str(i) for i in s.split()]
    for j in lst:
        l.append(j)
m=[]
for y in l:
    z=y.lower()
    m.append(z)
n=[]
for  k in m:
    if(k in n):
        continue
    else:
        n.append(k)
print(len(n))
h=sorted(n)
for j in h:
    print(j)
