for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=[]
    cnt=0
    for i in l:
        if cnt==n:
            break
        if i not in m:
            m.append(i)
            cnt+=1
    print(*m)
