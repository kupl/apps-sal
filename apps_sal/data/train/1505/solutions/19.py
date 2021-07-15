n=int(input())
a=list(map(int,input("").strip().split()))[:n]
s=list()
li=list()
k=0;
pos=0;
sik=list()
for l in range(len(a)):
    if a[l]==1:
        li.append('(')
        s.append('(')
    elif a[l]==2:
        s.append(')')
        if len(li)!=0:
            if k<len(li):
                pos=l;
                k=len(li)
            del li[len(li)-1]
        if len(li)==0:
            sik.append(s);
            s=list()
le=0;
for i in sik:
    if le<len(i):
        le=len(i);
se=0;
for i in sik:
    if le==len(i):
        break;
    se+=len(i);
print(k,pos,le,se+1)

