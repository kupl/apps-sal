for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in l:
        if(i>=(n-1)/2):
            c+=1
    print(c)
