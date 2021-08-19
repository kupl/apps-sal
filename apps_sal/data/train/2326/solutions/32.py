3.6
n = int(input())
a = [int(item) for item in input().split()]
awid = []
for (i, item) in enumerate(a):
    awid.append((item, i))
awid.sort(reverse=True)
bit = [0] * (n + 1)
cnt = [0] * (n + 1)


def bit_add(bit, x, w):
    while x <= n:
        bit[x] += w
        x += x & -x


def bit_sum(bit, x):
    ret = 0
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret


min_as = [-1] * n
min_a = 0
for (i, item) in enumerate(a):
    if item > min_a:
        min_as[i] = min_a
        min_a = item
ans = [0] * n
itr = 0
subbed = 0
for (i, item) in enumerate(min_as[::-1]):
    place = n - 1 - i
    if item != -1:
        while itr < n and awid[itr][0] > item:
            (val, index) = awid[itr]
            bit_add(bit, index + 1, val)
            bit_add(cnt, index + 1, 1)
            itr += 1
        ret = bit_sum(bit, n) - bit_sum(bit, place) - (bit_sum(cnt, n) - bit_sum(cnt, place)) * item - subbed
        ans[place] = ret
        subbed += ret
for item in ans:
    print(item)
