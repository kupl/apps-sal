# https://codeforces.com/contest/1208/problem/D

from sys import stdin, stdout
input = stdin.readline
# print = stdout.write

# si is the sum of elements before the i-th element that are smaller than the i-th element.

# For every i from N to 1, let's say the value of the si is x.
# So it means there are k smallest unused numbers whose sum is x.
# We simply put the k+1st number in the output permutation at this i, and continue to move left.

# BIT and binary lifting
# https://codeforces.com/contest/1208/submission/59526098


class BIT:
    def __init__(self, nums):
        # we store the sum information in bit 1.
        # so the indices should be 1 based.
        # here we assume nums[0] = 0
        self.nums = [0] * (len(nums))
        for i, x in enumerate(nums):
            if i == 0:
                continue
            self.update(i, x)

    def low_bit(self, x):
        return x & (-x)

    def update(self, i, diff):
        while i < len(self.nums):
            self.nums[i] += diff
            i += self.low_bit(i)

    def prefix_sum(self, i):
        ret = 0
        while i != 0:
            ret += self.nums[i]
            i -= self.low_bit(i)
        return ret

    def search(self, x):
        # find the index i such that prefix_sum(i) == x
        cur_index, cur_sum = 0, 0
        delta = len(self.nums) - 1
        while delta - self.low_bit(delta):
            delta -= self.low_bit(delta)

        while delta:
            m = cur_index + delta
            if m < len(self.nums):
                sm = cur_sum + self.nums[m]
                if sm <= x:
                    cur_index, cur_sum = m, sm
            delta //= 2
        return cur_index + 1


n = int(input())
bit = BIT(list(range(n + 1)))

ans = [0 for _ in range(n)]
nums = list(map(int, input().split()))
for i in range(n - 1, -1, -1):
    index = bit.search(nums[i])
    bit.update(index, -index)
    ans[i] = index
print(*ans)
