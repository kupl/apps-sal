T=int(input())
for _ in range(T):
    a=int(input())
    b=list(map(int,input().split()))
    c=int(input())
    for _ in range(c):
        d=list(map(int,input().split()))
        e=d[0]-1
        print(sum(b[e:d[1]]))

