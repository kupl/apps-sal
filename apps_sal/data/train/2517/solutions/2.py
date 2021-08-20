from collections import deque


class Solution:

    def tribonacci(self, n: int) -> int:
        if n > 0 and n < 3:
            return 1
        if n == 0:
            return 0
        queue = deque([0, 1, 1])
        t = 2
        while t != n:
            queue.append(sum(queue))
            queue.popleft()
            t += 1
        return queue[2]
