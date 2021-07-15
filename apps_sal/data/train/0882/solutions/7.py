# cook your dish here
for _ in range(int(input())):
    a=input()
    b=input()
    d=dict()
    ct=0
    for i in a:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    for j in b:
        if j in d.keys():
            if d[j]!=0:
                d[j]-=1
                ct+=1
    print(ct)
