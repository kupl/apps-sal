class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        \"\"\"
        Solution:
        #1 merge sort, time O (nlogn), space O(n) 
        
        \"\"\"
        # return self.mergeSort(nums)
        return self.heap_sort(nums)
    
    def mergeSort(self, nums):
        # exit
        if len(nums) <= 1:
            return nums
        # 向下取整
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        
        # merge two sub list
        ret = []
        l_idx = r_idx = 0
        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx] <= right[r_idx]:
                ret.append(left[l_idx])
                l_idx += 1
            else:
                ret.append(right[r_idx])
                r_idx += 1
        while l_idx < len(left):
            ret.append(left[l_idx])
            l_idx += 1
        while r_idx < len(right):
            ret.append(right[r_idx])
            r_idx += 1
        return ret
        
        
    def heap_sort(self, nums):
        # 调整堆
        # 迭代写法
        # def adjust_heap(nums, startpos, endpos):
        #     newitem = nums[startpos]
        #     pos = startpos
        #     childpos = pos * 2 + 1
        #     while childpos < endpos:
        #         rightpos = childpos + 1
        #         if rightpos < endpos and nums[rightpos] >= nums[childpos]:
        #             childpos = rightpos
        #         if newitem < nums[childpos]:
        #             nums[pos] = nums[childpos]
        #             pos = childpos
        #             childpos = pos * 2 + 1
        #         else:
        #             break
        #     nums[pos] = newitem

        # 递归写法
        def adjust_heap(nums, startpos, endpos):
            pos = startpos
            chilidpos = pos * 2 + 1
            if chilidpos < endpos:
                rightpos = chilidpos + 1
                if rightpos < endpos and nums[rightpos] > nums[chilidpos]:
                    chilidpos = rightpos
                if nums[chilidpos] > nums[pos]:
                    nums[pos], nums[chilidpos] = nums[chilidpos], nums[pos]
                    adjust_heap(nums, chilidpos, endpos)

        n = len(nums)
        # 建堆
        for i in reversed(range(n // 2)):
            adjust_heap(nums, i, n)
        # 调整堆
        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            adjust_heap(nums, 0, i)
        return nums

            
            
        
