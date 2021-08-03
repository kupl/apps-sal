class Solution:
    def maxheapify(self, a, heapsize, i):
        l, r = 2 * i + 1, 2 * i + 2
        leftisgreater = rightisgreater = False
        if l < heapsize and a[i] < a[l]:
            leftisgreater = True
        if r < heapsize and a[i] < a[r]:
            rightisgreater = True

        if leftisgreater and not rightisgreater:
            a[i], a[l] = a[l], a[i]
            self.maxheapify(a, heapsize, l)
        elif not leftisgreater and rightisgreater:
            a[i], a[r] = a[r], a[i]
            self.maxheapify(a, heapsize, r)
        elif leftisgreater and rightisgreater:
            if a[l] <= a[r]:
                a[i], a[r] = a[r], a[i]
                self.maxheapify(a, heapsize, r)
            else:
                a[i], a[l] = a[l], a[i]
                self.maxheapify(a, heapsize, l)

    def buildmaxheap(self, nums, heapsize):
        for i in reversed(range(len(nums) // 2)):
            self.maxheapify(nums, heapsize, i)

    def heapsort(self, nums):
        heapsize = len(nums)
        self.buildmaxheap(nums, heapsize)
        for i in range(len(nums)):
            nums[0], nums[heapsize - 1] = nums[heapsize - 1], nums[0]
            heapsize -= 1
            self.maxheapify(nums, heapsize, 0)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapsort(nums)
        return nums
