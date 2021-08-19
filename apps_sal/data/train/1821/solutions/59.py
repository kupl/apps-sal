class Solution:

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return i // 2 - 1 if not i % 2 else i // 2

    def maxheapify(self, a, heapsize, i):
        l = self.left(i)
        leftisgreater = False
        rightisgreater = False
        if l < heapsize:
            if a[i] < a[l]:
                leftisgreater = True
        r = self.right(i)
        if r < heapsize:
            if a[i] < a[r]:
                rightisgreater = True
        if leftisgreater or rightisgreater:
            if leftisgreater and (not rightisgreater):
                (a[i], a[l]) = (a[l], a[i])
                self.maxheapify(a, heapsize, l)
            elif not leftisgreater and rightisgreater:
                (a[i], a[r]) = (a[r], a[i])
                self.maxheapify(a, heapsize, r)
            elif leftisgreater and rightisgreater:
                if a[l] <= a[r]:
                    rightisgreater = True
                    leftisgreater = False
                else:
                    leftisgreater = True
                    rightisgreater = False
                if rightisgreater:
                    (a[i], a[r]) = (a[r], a[i])
                    self.maxheapify(a, heapsize, r)
                else:
                    (a[i], a[l]) = (a[l], a[i])
                    self.maxheapify(a, heapsize, l)

    def buildmaxheap(self, nums, heapsize):
        for i in reversed(range(len(nums) // 2)):
            self.maxheapify(nums, heapsize, i)

    def heapsort(self, nums):
        heapsize = len(nums)
        self.buildmaxheap(nums, heapsize)
        for i in range(len(nums)):
            (nums[0], nums[heapsize - 1]) = (nums[heapsize - 1], nums[0])
            heapsize -= 1
            self.maxheapify(nums, heapsize, 0)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapsort(nums)
        return nums
