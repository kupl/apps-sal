for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sum5=0
    sum10=0
    f=1
    if a[0]!=5:
        f=0
    else:
        for i in range(n):
            if a[i]==5:
                sum5+=1
            elif a[i]==10:
                if sum5<1:
                    f=0
                else:
                    sum5-=1
                    sum10+=1
            elif a[i]==15:
                if sum5<2 and sum10<1:
                    f=0
                else:
                    if sum5<2 and sum10>=1:
                        sum10-=1
                    elif sum5>=2 and sum10<1:
                        sum5-=2
                    else:
                        sum10-=1
    if f==1:
        print("YES")
    else:
        print("NO")
