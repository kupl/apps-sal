from bisect import bisect


class Solution:
    def sampleStats(self, counts: List[int]) -> List[float]:
        n = sum(counts)
        minimum = next(i for i in range(len(counts)) if counts[i])
        maximum = next(i for i in range(len(counts) - 1, -1, -1) if counts[i])
        mean = sum(i * counts[i] for i in range(1, 256)) / n
        mode = float(counts.index(max(counts)))
        for i in range(1, 256):
            counts[i] += counts[i - 1]
        median = 0.5 * (bisect(counts, n / 2) + bisect(counts, (n - 1) / 2))
        return [minimum, maximum, mean, median, mode]
