from sys import stdin

input = stdin.readline

q = int(input())

for ppppp in range(q):
    [n, k] = [int(item) for item in input().split(' ')]
    x = input()

    inf_seq = 'RGB'
    ptr = 0

    weights = []
    cost = [0, 0, 0]
    for i in range(k):
        dd = [0, 0, 0]
        for d in range(3):
            if x[i] != inf_seq[(i + d) % 3]:
                dd[d] = 1
                cost[d] += 1
        weights.append(dd)

    min_changes = min(cost)

    for i in range(k, n):
        dd = [0, 0, 0]
        for d in range(3):
            cost[d] -= weights[i - k][d]

            if x[i] != inf_seq[(i + d) % 3]:
                dd[d] = 1
                cost[d] += 1
        weights.append(dd)
        min_changes = min(min_changes, min(cost))

    print(min_changes)
