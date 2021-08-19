class Solution:

    def SequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(1, 10):
            for j in range(i + 1, 10):
                i = i * 10 + j
                if i > high:
                    break
                if i >= low:
                    res.append(i)
        return sorted(res)

    def sequentialDigits(self, low, high):
        out = []
        queue = deque(range(1, 10))
        while queue and queue[0] <= high:
            elem = queue.popleft()
            if low <= elem:
                out.append(elem)
            last = elem % 10
            if last < 9:
                queue.append(elem * 10 + last + 1)
        return out
