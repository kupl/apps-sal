class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) < 2:
            return nums
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)
        for i in range(n - 1, -1, -1):
            (nums[i], nums[0]) = (nums[0], nums[i])
            self.heapify(nums, i, 0)
        return nums

    def heapify(self, arr, n, i):
        largest = i
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        if leftChild < n and arr[largest] < arr[leftChild]:
            largest = leftChild
        if rightChild < n and arr[largest] < arr[rightChild]:
            largest = rightChild
        if largest != i:
            (arr[largest], arr[i]) = (arr[i], arr[largest])
            self.heapify(arr, n, largest)
