class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Take advantage of this problem to summarize all the sorting algorithms
        if not nums or len(nums) < 2:
            return nums
        
        return self.heapSort(nums)
    
    # Slow sorting algorithms
    
    def selection_sort(self, nums):
        # selection sort, every time we reduce the problem by moving the low boundary backwards by 1
        # 0: low is sorted and low: is not sorted
        # in-place without creating temp arrays O(n ^ 2)
        
        def select_smallest(nums, low):
            smallest_index = low
            for index in range(low + 1, len(nums)):
                if nums[index] < nums[smallest_index]:
                    smallest_index = index
            return smallest_index
            
        def swap(nums, i, j):
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
                
        for index in range(len(nums) - 1):
            target_index = select_smallest(nums, index)
            swap(nums, index, target_index)
             
        return nums
    
    def insert_sort(self, nums):
        # the sorted portion is [0: index], look at nums[index] and decide what is the best position to insert within [0: index]
        # (tricky) the shifting and finding the position to insert is done in the same loop
        for index in range(1, len(nums)):
            k = index
            while k > 0 and nums[k - 1]  > nums[k]:
                nums[k-1], nums[k] = nums[k], nums[k-1]
                k -= 1
        return nums
    
    def bubble_sort(self, nums):
        # each time we push the largest to the end, and then reduce the scope of bubbling
        def bubble(nums, end):
            for index in range(end):
                if nums[index] > nums[index + 1]:
                    nums[index], nums[index + 1] = nums[index + 1], nums[index]
        for end in range(len(nums) - 1, -1, -1):
            bubble(nums, end)
        return nums
    
    # Quicker sorting algorithms
    
    def quickSort(self, nums):
        # quick sort selects a pivot and partition the current list into two parts < pivot, greater than pivot
        # then recursion into each sub array for further sorting
        # 1. how to do the split
        # 2. how to do the recursion
        # 3. base cases
        def split(nums, low, high):
            # should return an index which partitions the data
            if low < 0 or high >= len(nums) or low >= high:
                return 
            pivot = nums[low]
            while low < high:
                # find the first element less than pivot
                while low < high and nums[high] > pivot:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] <= pivot:
                    low += 1
                nums[high] = nums[low]
            nums[low] = pivot
            return low 
        
        def recur(nums, low, high):
            if low >= high:
                return
            pivot_index = split(nums, low, high)
            recur(nums, low, pivot_index - 1)
            recur(nums, pivot_index + 1, high)
        recur(nums, 0, len(nums) - 1)
        return nums
    
    def mergeSort(self, nums):
        # spliting is easy, no need to have. a special function
        # merging is non-trivial, need to have a separate function. In-space is hard
    
        def merge(sub0, sub1):
            res = []
            m, n = len(sub0), len(sub1)
            p0 = p1 = 0
            while p0 < m and p1 < n:
                if sub0[p0] < sub1[p1]:
                    res.append(sub0[p0])
                    p0 += 1
                else:
                    res.append(sub1[p1])
                    p1 += 1
            while p0 < m:
                res.append(sub0[p0])
                p0 += 1
            while p1 < n:
                res.append(sub1[p1])
                p1 += 1
            return res
        
        if not nums or len(nums) < 2:
            return nums
        mid = len(nums) // 2
        left, right = self.mergeSort(nums[:mid]), self.mergeSort(nums[mid:])
        return merge(left, right)            
    
    def heapSort(self, nums):
        
        class Heap:
            def __init__(self, values=[]):
                self.values = values
                self.size = len(values)
                self.heapify()
                
            def _sift_down(self, i, n):
                if i >= n:
                    return
                candidate = i
                if i * 2 + 1 < n and self.values[2 * i + 1] > self.values[candidate]:
                    candidate = i * 2 + 1
                if i * 2 + 2 < n and self.values[2 * i + 2] > self.values[candidate]:
                    candidate = i * 2 + 2
                if candidate != i:
                    self.values[i], self.values[candidate] = self.values[candidate], self.values[i]
                    self._sift_down(candidate, n)
                    
            def heapify(self):
                if not self.values:
                    return
                n = self.size
                for index in range(n // 2, -1, -1):
                    self._sift_down(index, n)
                    
            def extract_max(self):
                ret = self.values[0]
                self.size -= 1
                self.values[0] = self.values[self.size]
                self._sift_down(0, self.size)
                return ret
            
        heap = Heap(nums)
        n = len(nums)
        result = []
        while heap.size:
            result.append(heap.extract_max())
        return result[::-1]
            
            
            
            
            
            
            
            
                
            
            
            
            
            
            
            

