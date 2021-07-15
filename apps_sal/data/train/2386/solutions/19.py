
tt = int(input())

lis = [-1] * 60

for loop in range(tt):

    n = int(input())
    p = list(map(int,input().split()))

    ans = []

    for i in p:
        if lis[i] == loop:
            continue
        else:
            ans.append(i)
            lis[i] = loop

    print(*ans)

