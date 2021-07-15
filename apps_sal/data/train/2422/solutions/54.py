class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        s = set([])
        m = 0
        for num in nums:
            x = num-1
            for y in s:
                p = x*y
                if m<p:
                    m = p
            s.add(x)
        return m

