def get_bit(diff, i):
    return 1 if ((i % 2 == 1 and diff <= 0) or (i % 2 == 0 and diff >= 0)) else 0


def swap_(i, j, a):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def swap(i, j, n, a, mask, S):
    change = 0
    swap_(i, j, a)
    set_index = set([i, j])

    if i < n - 1:
        set_index.add(i + 1)

    if j < n - 1:
        set_index.add(j + 1)

    for index in set_index:
        if index > 0:
            diff = a[index] - a[index - 1]
            bit_ = get_bit(diff, index)
            change += bit_ - mask[index]

    swap_(i, j, a)
    if S + change == 0:
        return 1
    return 0


n = int(input())
a = list(map(int, input().split()))

diff = [-1] + [x - y for x, y in zip(a[1:], a[:-1])]
mask = [get_bit(diff[i], i) for i in range(n)]

S = sum(mask)
first = -1
for i, x in enumerate(mask):
    if x == 1:
        first = i
        break

cnt = 0
for second in range(n):
    if swap(first, second, n, a, mask, S) == 1:
        cnt += 1

    if first != 0 and swap(first - 1, second, n, a, mask, S) == 1:
        cnt += 1

if first != 0 and swap(first - 1, first, n, a, mask, S) == 1:
    cnt -= 1

print(cnt)

# 9
# 1 2 3 4 5 6 7 8 9

# 10
# 3 2 1 4 1 4 1 4 1 4

# 4
# 200 150 100 50

# 5
# 2 8 4 7 7
