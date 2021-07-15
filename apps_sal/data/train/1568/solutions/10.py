# cook your dish here
for _ in range(int(input())):
    c=0
    n=int(input())
    num=list(map(int,input().split()))
    for i in num:
        if i>=n//2:
            c+=1
    print(c)
