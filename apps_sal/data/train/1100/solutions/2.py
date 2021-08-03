for i in range(int(input())):
    giv = [int(i) for i in input().split()]
    tar = [int(i) for i in input().split()]
    diff = set()
    f = 0
    c = 0
    s = 0
    for i in range(3):
        if tar[i] - giv[i] == 0:
            c += 1
        elif tar[i] - giv[i] < 0:
            f = 1
            break
        else:
            s += tar[i] - giv[i]
    if f == 1:
        print(-1)
    else:
        print(s)
