# author dragonwarrior8 :D
# UMEED!! Lets make it yellow 5*
T=int(input())
while T>0:
    T-=1
    N=int(input())
    A=list(map(int,input().split()))
    sum1=sum(A)
    cntzero = 0

    for i in range(N):
        if A[i]==0:
            cntzero+=1
        else:
            break
    val = 0
    pos=0
    for i in range(cntzero,N,1):
        if val<sum1:
            val+=A[i]
            pos+=1
        else:
            break
    if pos==0:
        print("1")
    else:
        print(pos)

