def update(index, value, bi_tree):
    while index < len(bi_tree):
        bi_tree[index] += value
        index += index & -index


def get_sum(index, bi_tree):
    ans = 0
    while index > 0:
        ans += bi_tree[index]
        index -= index & -index
    return ans


def get_range_sum(left, right, bi_tree):
    ans = get_sum(right, bi_tree) - get_sum(left - 1, bi_tree)
    return ans


def solve(x):
    s = set()
    res = 1
    i = 2
    while i * i <= x:
        count = 0
        while x % i == 0:
            x = x // i
            count += 1
        if count % 2:
            s.add(i)
        i += 1
    if x > 0:
        s.add(x)
    return s


n = int(input())
l = [0] + [int(i) for i in input().split()]
bit = [[0 for i in range(n + 1)] for i in range(101)]
for i in range(1, n + 1):
    s = solve(l[i])
    for j in s:
        update(i, 1, bit[j])
q = int(input())
for i in range(q):
    (k, a, b) = [int(i) for i in input().split()]
    if k == 1:
        f = 1
        for i in range(2, 100):
            res = get_range_sum(a, b, bit[i])
            if res % 2:
                f = 0
                break
        if f:
            print('YES')
        else:
            print('NO')
    else:
        s = solve(b)
        for j in s:
            update(a, 1, bit[j])
