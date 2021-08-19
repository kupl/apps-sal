from bisect import bisect_left
INF = float('inf')
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def calc_bit(k):
    mod = 1 << k + 1
    amod = [a & mod - 1 for a in A]
    bmod = [b & mod - 1 for b in B]
    amod.sort()
    bmod.sort()
    ret = 0
    b01 = bisect_left(bmod, (1 << k) - amod[0])
    b10 = bisect_left(bmod, (2 << k) - amod[0])
    b11 = bisect_left(bmod, (3 << k) - amod[0])
    for a in range(len(amod)):
        while b01 - 1 >= 0 and bmod[b01 - 1] >= (1 << k) - amod[a]:
            b01 -= 1
        while b10 - 1 >= 0 and bmod[b10 - 1] >= (2 << k) - amod[a]:
            b10 -= 1
        while b11 - 1 >= 0 and bmod[b11 - 1] >= (3 << k) - amod[a]:
            b11 -= 1
        ret += b10 - b01
        ret += N - b11
    return ret % 2


ans = 0
for i in range(30):
    ans += calc_bit(i) * (1 << i)
print(ans)
