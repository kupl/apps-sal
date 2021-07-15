# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    mi=min(l)
    ans=n/mi
    if(ans==int(ans)):
        print(int(ans))
    else:
        print(int(ans)+1)
