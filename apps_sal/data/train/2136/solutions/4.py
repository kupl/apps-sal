def find(A):
    ##A is a list of non-increasing number
    on=1
    ans=0
    for x in A:
        if on==1:
            ans+=x//2+x%2
            on=0
        else:
            ans+=x//2
            on=1
    return min(ans,sum(A)-ans)
n=int(input())
A=list(map(int,input().strip().split()))
print(find(A))
