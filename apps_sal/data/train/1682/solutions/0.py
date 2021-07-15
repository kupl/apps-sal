l=list(map(int,input()))
t=-1
x=-1
y=-1
for i in range(len(l)):
    s=l[i]
    a=i+1
    b=i+1
    for j in range(i+1,len(l)):
        if l[i]<l[j]:
            s=s+l[j]
            b=j+1
        else:
            break
    if s>t:
        t=s
        x=a
        y=b
print(t,end=":")
print(x,y,sep="-")
