class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapSort(nums)
        return nums
  
    
\t# @quickSort
    def quickSort(self, nums):
        
        def partition(head, tail):
            
            if head >= tail: return
            
            l, r = head, tail
            m = (r - l) // 2 + l
            pivot = nums[m]
            
            while r >= l:
                while r >= l and nums[l] < pivot: 
                    l += 1
                while r >= l and nums[r] > pivot: 
                    r -= 1
                    
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                    
            partition(head, r)
            partition(l, tail)

        partition(0, len(nums)-1)
        return nums
     
\t# @mergeSort
    
    def mergeSort(self, nums): 
        
        if len(nums) > 1: 
            
            mid = len(nums)//2
            
            L = nums[:mid] 
            R = nums[mid:] 

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1
 
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1
   
   # @heapSort
    
    def heapSort(self, nums):
        
        def heapify(nums, n, i): 
            
            l = 2 * i + 1 #left
            r = 2 * i + 2 #right
\t\t\t
            largest = i
            
            if l < n and nums[largest] < nums[l]: 
                largest = l 

            if r < n and nums[largest] < nums[r]: 
                largest = r 

            if largest != i: #if its not equal to root
                nums[i], nums[largest] = nums[largest], nums[i] #swap
                
                heapify(nums, n, largest)
                
        n = len(nums) 

        for i in range(n//2+1)[::-1]:  #starting from the last non leaf node and going until the top
            heapify(nums, n, i) 

        for i in range(n)[::-1]: 
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)
