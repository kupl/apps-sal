try:
    from collections import Counter
    for i in range(int(input())):
        n=int(input())
        l=list(map(str,input().split()))
        c=list(Counter(l).items())
        x=max(list(Counter(l).values()))
        y=[]
        for j,k in c:
            if k==x:
                y.append(j)
        print(min(y))
except:
    pass
