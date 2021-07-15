t=eval(input())
for i in range(1,t+1):
    a=input();l=[]
    for i in range(len(a)-1):
        l+=[a[i]+a[i+1]]
    l=set(l)
    print(len(l))
