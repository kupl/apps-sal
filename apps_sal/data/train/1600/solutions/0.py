t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    d={}
    for i in range(n):
        if arr[i] in d:
            d[arr[i]].append(i)
        else:
            d[arr[i]]=[i]
    q=int(input())
    for i in range(q):
        m=int(input())
        if len(d[m])==1:
            print(n)
        elif len(d[m])==2:
            print(min((d[m][1]-d[m][0]),((n-d[m][1])+d[m][0])))
        else:
            k=100000
            for j in range(len(d[m])-1):
                if (d[m][j+1]-d[m][j])<k:
                    k=d[m][j+1]-d[m][j]
                else:
                    pass
            print(min(k,((n-d[m][len(d[m])-1])+d[m][0])))
            
                

