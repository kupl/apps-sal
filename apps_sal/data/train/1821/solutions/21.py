from random import shuffle


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        size = 1
        aux = [0] * len(nums)
        while size < len(nums):
            for lo in range(0, len(nums) - size, 2 * size):
                hi = min(len(nums) - 1, lo + 2 * size - 1)
                aux[lo:hi + 1] = nums[lo:hi + 1]
                i, j = lo, lo + size
                for k in range(lo, hi + 1):
                    if i > lo + size - 1:
                        nums[k] = aux[j]
                        j += 1
                    elif j > hi:
                        nums[k] = aux[i]
                        i += 1
                    elif aux[i] > aux[j]:
                        nums[k] = aux[j]
                        j += 1
                    else:
                        nums[k] = aux[i]
                        i += 1
            size *= 2
        return nums
