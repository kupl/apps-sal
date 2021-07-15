class Solution:
    def _merge(self, list1, list2):
        tmp = []
        while list1 and list2:
            (tmp.append(list1.pop(0))
             if list1[0] < list2[0]
             else tmp.append(list2.pop(0)))
        return tmp + (list1 or list2)

    def sortArray(self, nums: List[int]) -> List[int]:
        pivot = len(nums) // 2
        return (nums
                if len(nums) < 2
                else self._merge(self.sortArray(nums[:pivot]),
                                self.sortArray(nums[pivot:])))
