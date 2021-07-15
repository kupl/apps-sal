# cook your dish here
try:
    t=int(input())
    l1=[]
    l2=[]
    n1=0
    n2=0
    for i in range(t):
        x,y=list(map(int,input().split()))
        n1+=x
        n2+=y
        if n1>n2:
            l1.append(n1-n2)
            l2.append(0)
        else:
            l1.append(0)
            l2.append(n2-n1)
    m1=max(l1)
    m2=max(l2)
    if m1>m2:
        print(1,m1)
    else:
        print(2,m2)
except:pass

