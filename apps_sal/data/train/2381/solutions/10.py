def one():
    return int(input())


def more():
    return list(map(int, input().split()))


for _ in range(one()):
    s = input() + 'R'
    cur = 0
    mx = -1
    for ind, i in enumerate(s):
        if i == 'R':
            d = ind + 1 - cur
            mx = max(mx, d)
            cur = ind + 1

    print(mx)

