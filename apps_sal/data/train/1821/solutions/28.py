def merge(list1, list2):
    merged = []
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] < list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))
    if len(list1) == 0:
        return merged + list2
    else:
        return merged + list1
        

class Solution:
    # Merge Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            return merge(self.sortArray(nums[:len(nums) // 2]), self.sortArray(nums[len(nums) // 2:]))
        

