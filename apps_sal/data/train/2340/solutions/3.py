import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())

    P = list(map(int, input().split()))

    MAX = -1
    L = []
    count = 0
    for p in P:
        if p > MAX:
            L.append(count)
            MAX = p
            count = 1
        else:
            count += 1
    L.append(count)

    # print(L)

    DP = 1

    MAX = (1 << (n + 1)) - 1

    for i in L:
        DP = (DP | DP << i) & MAX

    # print(bin(DP))

    if DP & (1 << n) != 0:
        print("YES")
    else:
        print("NO")
