for _ in range(int(input())):
    lens = int(input())
    has = set([int(x) for x in input().split()])
    rets = [0] * lens
    for i in range(lens):
        if i in has:
            rets[i] = i

    print(*rets)
