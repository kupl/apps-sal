class Solution:

    def sampleStats(self, count: List[int]) -> List[float]:
        tmp_ = [sum(count[:i + 1]) for i in range(256)]
        return [next((i for i in range(256) if count[i])) * 1.0, next((i for i in range(255, -1, -1) if count[i])) * 1.0, sum((i * v for (i, v) in enumerate(count))) / sum(count) * 1.0, (bisect.bisect(tmp_, (sum(count) - 1) / 2) + bisect.bisect(tmp_, sum(count) / 2)) / 2.0, float(count.index(max(count)))]
