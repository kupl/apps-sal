class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freqs = [0] * (len(nums) + 1)
        for (s, e) in requests:
            freqs[s] += 1
            freqs[e + 1] -= 1
        freqs.pop()
        nzFreqs = []
        f = 0
        for (i, (x, n)) in enumerate(zip(freqs, nums)):
            f += x
            if f > 0:
                nzFreqs.append(f)
            nums[i] = -n
        heapq.heapify(nums)
        nzFreqs.sort(reverse=True)
        result = 0
        for f in nzFreqs:
            result += f * heapq.heappop(nums)
        return -result % 1000000007
