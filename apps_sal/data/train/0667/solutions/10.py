for _ in range(int(input())):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))


    for i in range(n-1,-1,-1):

        ans=(d//a[i])
        ans1=ans*a[i]
        mini=ans1
        d=ans1
        ##p##rint(mini,d)
    print(mini)
