class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.counts = [Counter() for _ in range(self.n * 2)]
        for i, num in enumerate(arr):
            self.counts[i + self.n][num] += 1
        for i in range(self.n)[::-1]:
            self.counts[i] = self.counts[i * 2] + self.counts[i * 2 + 1]

    def query(self, left: int, right: int, threshold: int) -> int:
        left += self.n
        right += self.n + 1
        c = Counter()
        while left < right:
            if left % 2 == 1:
                c += self.counts[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                c += self.counts[right]
            right //= 2
            left //= 2
        topcount, topnum = max((ct, num) for num, ct in list(c.items()))
        return topnum if topcount >= threshold else -1
