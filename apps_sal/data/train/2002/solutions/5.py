def func(a):
    b=[0]*26
    for i in range(len(a)):
        b[ord(a[i])-ord("a")]+=1
    c=0
    for i in b:
        if i==1:
            c=c+1
    return c



s=input()
n=len(s)
a={}
for i in range(n):
    a[s[i]]=[]
for i in range(n):
    a[s[i]].append(i)
c=0
for i in a:
    if len(a[i])==1:
        c=c+1
    else:
        e=[]
        for j in range(n):
            b=[]
            d=0
            for k in a[i]:
                b.append((s[(k+j)%n]))
            d=d+func(b)
            e.append(d)
        c=c+max(e)
    
print(c/n)
