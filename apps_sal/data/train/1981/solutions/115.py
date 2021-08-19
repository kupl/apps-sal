class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        """
        factors = [0]*len(nums)
        for a,b in requests:
            for i in range(a,b+1):
                factors[i] += 1
        factors.sort()
        nums.sort()
        out = 0
        for i in range(len(nums)):
            out = (out + nums[i]*factors[i])%(10**9+7)
        return out
        """
        pts = []
        for (a, b) in requests:
            pts.append((a, -1))
            pts.append((b, +1))
        pts.sort()
        dic = defaultdict(int)
        (factor, prev) = (0, 0)
        for (a, d) in pts:
            if d == -1:
                dic[factor] += a - prev
                prev = a
            else:
                dic[factor] += a + 1 - prev
                prev = a + 1
            factor += -d
        nums.sort(reverse=True)
        (prev, out) = (0, 0)
        dic = sorted(list(dic.items()), key=lambda x: x[0], reverse=True)
        for (factor, length) in dic:
            for k in range(prev, prev + length):
                out = (out + factor * nums[k]) % (10 ** 9 + 7)
            prev += length
        return out
