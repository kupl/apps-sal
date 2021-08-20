class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        (left, right) = (self.mergeSort(nums[:mid]), self.mergeSort(nums[mid:]))
        return merge(left, right)

    def merge(le, ri):
        (i, j) = (0, 0)
        res = []
        while i < len(le) and j < len(ri):
            if le[i] < ri[j]:
                res.append(le[i])
                i += 1
            else:
                res.append(ri[j])
                j += 1
        res.append(le[i:] if j == len(ri) - 1 else ri[j:])
        print(res)
        return res

    def quickSort(self, nums, start, end):
        random.shuffle(nums)

        def sort(nums, start, end):
            if end <= start:
                return
            (i, j) = (start, end)
            p = start
            curNum = nums[start]
            while p <= j:
                if nums[p] < curNum:
                    (nums[i], nums[p]) = (nums[p], nums[i])
                    i += 1
                    p += 1
                elif nums[p] > curNum:
                    (nums[p], nums[j]) = (nums[j], nums[p])
                    j -= 1
                else:
                    p += 1
            sort(nums, start, i - 1)
            sort(nums, j + 1, end)
        sort(nums, start, end)
