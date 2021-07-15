# cook your dish here
from collections import defaultdict
for _ in range(int(input())):


    n=int(input())
    a=list(map(int,input().split()))
    d= defaultdict(lambda:-1)
    d1= defaultdict(lambda:-1)
    maxi=-1
    for i in range(len(a)):

        x=d[a[i]]
        if x!=-1 and (i-x==1 or i-x==2) :
            d1[a[i]]+=1
        else:
            d1[a[i]]=0
        d[a[i]]=i
        maxi=max(maxi,d1[a[i]])

    print(maxi)

