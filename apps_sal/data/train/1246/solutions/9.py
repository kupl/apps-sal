for _ in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    l1.sort()
    l2=list(map(int,input().split()))
    l2.sort()
    if(l1[n-1]!=l2[n-1]):
        print("YES")
    else:
        print("NO")

