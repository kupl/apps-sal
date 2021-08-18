class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        import math
        from collections import deque

        deq = deque([i for i in range(1, 10)])
        res = []

        while deq:
            num = deq.popleft()

            if math.pow(10, n - 1) <= num < math.pow(10, n):
                res.append(num)
            else:
                targets = [num % 10 - k, num % 10 + k] if k > 0 else [num % 10]
                for target in targets:
                    if 0 <= target <= 9:
                        deq.append(num * 10 + target)

        return res
