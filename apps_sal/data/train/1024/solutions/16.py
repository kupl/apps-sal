# cook your dish here
def fun1(S,N,K,R):
    total=K
    for _ in range(1,N):
        K=K*R
        total+=K
    return (S-total)    

final=0
T=int(input())

for i in range(T):
    S,N,K,R=map(int,input().split())
    slices_required=fun1(S,N,K,R)
    if(slices_required >= 0):
        print("POSSIBLE",end=" ")
        print(slices_required)
    else:
        print("IMPOSSIBLE",end=" ")
        print(abs(slices_required))
    final+=slices_required
if(final>=0):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

