class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        counts = collections.Counter()
        A = []
        for (s, e) in requests:
            A.append((s, -1))
            A.append((e, 1))
        A.sort()
        (freq, h, last) = ([0] * n, 0, -1)
        for (index, direction) in A:
            if last >= 0:
                for i in range(last + 1, index):
                    freq[i] = h
            last = index
            if direction == -1:
                h += 1
                freq[index] = max(freq[index], h)
            else:
                freq[index] = max(freq[index], h)
                h -= 1
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        idx = res = 0
        for v in freq:
            res += nums[idx] * v
            idx += 1
        return res % (10 ** 9 + 7)
