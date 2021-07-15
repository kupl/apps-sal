t=int(input())
for _ in range(t):
    S=set(input().strip())
    n=int(input().strip())
    a=set(input().strip().split(" "))
    g=True
    for i in S:
        if(i not in a):
            g=False
    if(g):
        print(1)
    else:
        print(0)
