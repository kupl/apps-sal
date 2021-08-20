class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(a, b):
            l1 = l2 = 0
            (r1, r2) = (len(a), len(b))
            (i, j) = (l1, l2)
            out = []
            while i < r1 or j < r2:
                if j == r2 or (i < r1 and a[i] < b[j]):
                    out.append(a[i])
                    i += 1
                elif j < r2:
                    out.append(b[j])
                    j += 1
            return out
        skip_interval = 1
        while skip_interval < len(nums):
            for i in range(0, len(nums), 2 * skip_interval):
                middle = i + skip_interval
                nums[i:i + 2 * skip_interval] = merge(nums[i:middle], nums[middle:middle + skip_interval])
            skip_interval *= 2
        return nums
