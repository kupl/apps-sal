for _ in range(int(input())):
    l = list(map(int, input().split()))
    for i in range(l[-2] - 1):
        if((i + 1) % l[2] == 0):
            l[1] += l[-1]
        l[0] += l[1]
    print(l[0])
