for tc in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    trump = 1
    tmp1 = 0
    for i in A:
        if trump and i % 2 == 0:
            trump = 0
        elif i % 2 == 0:
            tmp1 += 2
        else:
            tmp1 += 1

    trump = 1
    tmp2 = 0
    for i in A:
        if trump and i % 2:
            trump = 0
        elif i % 2:
            tmp2 += 2
        else:
            tmp2 += 1

    print(min(tmp1, tmp2))
