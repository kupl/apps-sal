def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapify(nums, n, i):
    l = 2 * i
    r = 2 * i + 1
    largest = i
    
    if l < n and nums[l] > nums[largest]:
        largest = l
    if r < n and nums[r] > nums[largest]:
        largest = r
    if largest != i:
        swap(nums, i, largest)
        heapify(nums, n, largest)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # build heap
        n = len(nums)
        
        # n // 2 -> 0
        # building maximizing heap
        for i in range(n // 2, -1, -1):
            heapify(nums, n, i)
        
        for i in range(n - 1, -1, -1):
            swap(nums, 0, i)
            heapify(nums, i, 0)
        
        return nums
        # do the heap sort
        

