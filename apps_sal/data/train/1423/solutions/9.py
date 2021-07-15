for _ in range(int(input())):
    num=int(input())
    lst=list(map(int,input().split()))
    n=int(input())
    a=lst[n-1]
    lst.sort()
    for i in range(num):
        if a==lst[i]:
            print(i+1)
            break# cook your dish here

