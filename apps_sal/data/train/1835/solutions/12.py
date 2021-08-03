import itertools


class Solution:
    def step(self, n, k):
        d = n % 10
        b = n * 10

        if k == 0:
            yield b + d
        if d < d + k < 10:
            yield b + d + k
        if 0 <= d - k < d:
            yield b + d - k

    def solve(self, nums, n, k):
        if n == 1:
            return nums
        soln = [self.step(x, k) for x in nums]
        return itertools.chain.from_iterable([self.solve(x, (n - 1), k) for x in soln])

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        seed = [x for x in range(1, 10) if x + k < 10 or 0 <= x - k < 10]
        return list(self.solve(seed, n, k))
