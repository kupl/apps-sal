class Solution:

    def countLargestGroup(self, n: int) -> int:

        def sum_num(n):
            res = n % 10
            while n > 0:
                res += (n := (n // 10)) % 10
            return res
        groups = defaultdict(int)
        for i in range(1, n + 1):
            groups[sum_num(i)] += 1
        high = max(groups.values())
        return sum((1 for v in groups.values() if v == high))
