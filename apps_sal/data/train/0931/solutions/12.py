# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    s1=0
    for i in l1:
        if i%2==0:
            s1=s1+i
    print(s1)
