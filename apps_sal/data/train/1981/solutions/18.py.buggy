class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        '''
        requests can be converted to a frequency for each spot.
        Then the highest frequency spot should get the largest item, 
        and continue to the next largest item.
        '''
        s = sorted([a for a, _ in requests])
        e = sorted([a for _, a in requests])
\t\t
        freq = [bisect_right(s, i) - bisect_left(e, i) for i in range(len(nums))]
\t\t\t
        res = sum(f * n for f, n in zip(sorted(freq), sorted(nums)))
        return res % int(1e9 + 7)
