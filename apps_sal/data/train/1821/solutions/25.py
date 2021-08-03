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


def build_heap(nums):
    n = len(nums)
    for i in range(n // 2, -1, -1):
        heapify(nums, n, i)


def heap_sort(nums):
    n = len(nums)
    for i in range(n - 1, -1, -1):
        swap(nums, 0, i)
        heapify(nums, i, 0)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        build_heap(nums)
        heap_sort(nums)
        return nums
