class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # partition and return pivot index
        def partition(nums, low, high):
            p = nums[low]
            
            # i points the last one in region 1
            i,j = low, low+1
            while j <= high:
                if p > nums[j]:
                    # swap the first one in region 2 with current one 
                    # which should be in region 1
                    # then move i forward
                    nums[i+1], nums[j] = nums[j], nums[i+1]
                    i += 1
                j += 1
                
            # swap the pivot number with last one in region 1
            nums[i], nums[low] = nums[low], nums[i]
        
            return i
                
        # quicksort implementation
        def quickSort(nums, low, high):

            if low < high:
                # get pivot index
                pivot_ind = partition(nums, low, high)
                #print (pivot_ind, nums)

                # recursively call left and right part
                quickSort(nums,low, pivot_ind-1)
                quickSort(nums,pivot_ind+1, high)
        
        # now invoke quick sort
        low,high = 0, len(nums)-1
        quickSort(nums, low, high)
        return nums
