class Solution:

    def specialArray(self, nums: List[int]) -> int:
        freq = collections.Counter()
        (i, cnt) = (1, 0)
        for num in nums:
            freq[num] += 1
            if num >= i:
                cnt += 1
            if cnt == i:
                cnt -= freq[i]
                i += 1
        return -1 if cnt + freq[i - 1] != i - 1 else i - 1
