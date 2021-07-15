t=int(input())
l=[100,50,10,5,2,1]
for k in range(t):
    c=0
    s=0
    n=int(input())
    for j in range(6):
        s=int(n/l[j])
        c=c+s
        n=n-(s*l[j])
    print(c)
