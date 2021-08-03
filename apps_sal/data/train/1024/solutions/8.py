total, possible, impossible = 0, 0, 0
for i in range(int(input())):
    N, S, K, R = list(map(int, input().split()))
    total = total + N
    points = K
    sum = K
    for j in range(S - 1):
        points = points * R
        sum += points

    if sum <= N:
        possible = possible + N - sum
        print('POSSIBLE', N - sum)
    else:
        impossible = impossible + sum - N
        print('IMPOSSIBLE', sum - N)

if possible >= impossible:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
