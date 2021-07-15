t=int(input())
i=1 
while(i<=t):
    lst=list(map(int,input().strip().split()))
    a=lst.index(-1)
    lst1=lst[0:(a)]
    a1=len([j for j in lst1 if j>30])
    lst2=[k for k in lst1 if (k%2==0)]
    lst3=[0]*len(lst2)
    s=0 
    for l in range(0,len(lst2)):
        lst3[l]=(lst1.index(lst2[l])+1)
        s=s+(lst2[l]*lst3[l])
    ans=s/sum(lst3)
    print(a1,"{0:.2f}".format(ans))
    i+=1 
    

