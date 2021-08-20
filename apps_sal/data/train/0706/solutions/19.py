import sys


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


for t in range(int(input())):
    (N, K) = get_ints()
    B = get_array()
    flag = 1
    w = 0
    for i in range(N):
        if B[i] > K:
            flag = 0
            break
        elif w + B[i] <= K:
            w += B[i]
        else:
            w = B[i]
            flag += 1
    if flag == 0:
        print('-1')
    else:
        print(flag)
