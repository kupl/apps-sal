# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    pos=[]
    for i in range(len(a)):
        if a[i]==1:
            pos.append(i)
    for i in range(1,len(pos)):
        if pos[i]-pos[i-1]<6:
            print('NO')
            break
    else:
        print('YES')
