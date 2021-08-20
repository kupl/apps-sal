from sys import stdin, stdout
input = stdin.readline


class BIT:

    def __init__(self, nums):
        self.nums = [0] * len(nums)
        for (i, x) in enumerate(nums):
            if i == 0:
                continue
            self.update(i, x)

    def low_bit(self, x):
        return x & -x

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
        (cur_index, cur_sum) = (0, 0)
        delta = len(self.nums) - 1
        while delta - self.low_bit(delta):
            delta -= self.low_bit(delta)
        while delta:
            m = cur_index + delta
            if m < len(self.nums):
                sm = cur_sum + self.nums[m]
                if sm <= x:
                    (cur_index, cur_sum) = (m, sm)
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
