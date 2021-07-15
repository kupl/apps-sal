for _ in range(int(input())):
    t1=int(input())
    ta1=list(map(int,input().split()))
    d1=int(input())
    da1=list(map(int,input().split()))
    t2=int(input())
    ta2=list(map(int,input().split()))
    d2=int(input())
    da2=list(map(int,input().split()))
    if(set(ta2).issubset(set(ta1)) and set(da2).issubset(set(da1))):
        print("yes")
    else:
        print("no")
