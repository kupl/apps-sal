from operator import itemgetter


def get_one_max(arr, resource):
    res = 0
    for beauty, _ in [x for x in arr if x[1] <= resource]:
        res = max(res, beauty)
    return res


def get_two_max(arr, resource):
    arr.sort(key=itemgetter(1))
    best = [-1] * (resource + 1)
    ptr = 0
    for index, (beauty, price) in enumerate(arr):
        if price > resource:
            break
        while ptr < price:
            ptr += 1
            best[ptr] = best[ptr - 1]
        if best[ptr] == -1 or arr[best[ptr]][0] < beauty:
            best[ptr] = index

    while ptr < resource:
        ptr += 1
        best[ptr] = best[ptr - 1]

    res = 0
    for index, (beauty, price) in enumerate(arr):
        rest = resource - price
        if rest <= 0:
            break
        if best[rest] == -1 or best[rest] == index:
            continue
        res = max(res, beauty + arr[best[rest]][0])

    return res


n, coins, diamonds = list(map(int, input().split()))

with_coins = []
with_diamonds = []

for i in range(n):
    beauty, price, tp = input().split()
    if tp == 'C':
        with_coins.append((int(beauty), int(price)))
    else:
        with_diamonds.append((int(beauty), int(price)))

with_coins_max = get_one_max(with_coins, coins)
with_diamonds_max = get_one_max(with_diamonds, diamonds)
ans = 0 if with_coins_max == 0 or with_diamonds_max == 0 \
    else with_coins_max + with_diamonds_max
ans = max(ans, get_two_max(with_coins, coins))
ans = max(ans, get_two_max(with_diamonds, diamonds))

print(ans)
