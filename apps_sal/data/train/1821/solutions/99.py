class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.mergeSort(nums)
        self.quickSort(nums, 0, len(nums)-1)
        return nums
    
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        mid = len(nums)//2
        left, right = self.mergeSort(nums[:mid]), self.mergeSort(nums[mid:])
        return merge(left, right)
    def merge(le, ri):
        i, j = 0, 0
        res = []
        while i < len(le) and j < len(ri):
            if le[i] < ri[j]:
                res.append(le[i])
                i += 1
            else:
                res.append(ri[j])
                j += 1
        res.append(le[i:] if j == len(ri)-1 else ri[j:])
        print(res)
        return res
    
    def quickSort(self, nums, start, end):
        random.shuffle(nums)
        def sort(nums, start, end):
            if end <= start:
                return
            i, j = start, end
            p = start
            curNum = nums[start]
            while p <= j:
                if nums[p] < curNum:
                    nums[i], nums[p] = nums[p], nums[i]
                    i += 1
                    p += 1
                elif nums[p] > curNum:
                    nums[p], nums[j] = nums[j], nums[p]
                    j -= 1
                else: #nums[p]==curNum
                    p += 1   
            sort(nums, start, i-1)
            sort(nums, j+1, end)
        sort(nums,start,end)
        # def parition(nums, i, j):
        #     mid = i + (j-1-i)//2
        #     nums[j-1], nums[mid] = nums[mid], nums[j-1]
        #     for idx in range(i, j):
        #         if nums[idx] < nums[j-1]:
        #             nums[i], nums[idx] = nums[idx], nums[i]
        #             i += 1
        #     nums[j-1], nums[i] = nums[i], nums[j-1]
        #     # while i <= j-2 and nums[i] == nums[i+1]:
        #     #     i += 1
        #     return i
                

        
#         def partition(A, I, J):
#             A[J-1], A[(I + J - 1)//2], i = A[(I + J - 1)//2], A[J-1], I
#             for j in range(I,J):
#                 if A[j] < A[J-1]: A[i], A[j], i = A[j], A[i], i + 1
#             A[J-1], A[i] = A[i], A[J-1]
#             return i
        
        

