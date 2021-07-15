for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    flag=0
    for i in range(len(a)-2):
        if len(set(a[i:i+3]))==1:
            print('Yes')
            flag=1
            break
        else:
            flag=0
    if flag==0:
        print('No')
