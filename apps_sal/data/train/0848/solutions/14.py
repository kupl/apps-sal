for _ in range(int(input())):
    n=int(input())
    x=list(map(int, input().split()))
    x.append(x[0])
    x.append(x[1])
    n+=2
    s=0
    if(n<=3):
        print(sum(x))
        continue
    for i in range(n-3):
        if(sum(x[i:i+3])>s):
            s=sum(x[i:i+3])
    print(s)
