for l in range(int(input())):
    a=int(input())
    s=list(map(int,input().split()))
    m=0
    for i in range(a):
        if s[i]>=(a/2):
            m=m+1
    print(m)
