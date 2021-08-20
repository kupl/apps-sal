def rii():
    return list(map(int, input().strip().split(' ')))


def ril():
    return list(map(int, input().strip().split(' ')))


def ri():
    return int(input().strip())


def rs():
    return eval(input())


T = ri()
for _ in range(T):
    N = ri()
    l = [0 for i in range(8)]
    for i in range(N):
        (nb, S) = rii()
        if nb < 9:
            l[nb - 1] = max(S, l[nb - 1])
    print(sum(l))
