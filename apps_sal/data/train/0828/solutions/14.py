# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = 0
    flg = 0
    for i in range(n):
        if l[i]==0:
            c+=1100
            flg=1
        elif l[i]==1:
            if flg==1:
                c+=100
    print(c)
