class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        tmp = [0 for _ in range(len(nums))]
        self.merge_sort(nums, 0, len(nums)-1, tmp)
        return nums
        
        
    def merge_sort(self, nums, left, right, tmp):
        if left >= right:
            return
        mid = (left + right) // 2
        
        self.merge_sort(nums, left, mid, tmp)
        self.merge_sort(nums, mid+1, right, tmp)
        self.merge(nums, left, right, tmp)

        
        
    def merge(self, nums, left, right, tmp):
        
        n = right - left + 1
        mid = (left + right) // 2
        i, j = left, mid +1
        
        for k in range(n):
            # j>right means right side is used up
            if i <= mid and (j > right or nums[i]<=nums[j]):
                tmp[k] = nums[i]
                i += 1
            else:
                tmp[k] = nums[j]
                j += 1
        
        for k in range(n):
            nums[left + k] = tmp[k]
        

