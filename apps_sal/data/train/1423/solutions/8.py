t=int(input())
for i in range(t):
    num=int(input())
    lst=list(map(int,input().split()))
    pos=int(input())
    x=lst[pos-1]
    lst.sort()
    print(lst.index(x)+1)
