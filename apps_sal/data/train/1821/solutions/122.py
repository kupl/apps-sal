class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(l1, l2):
            p1 = p2 = 0
            new_list = []
            while p1 < len(l1) or p2 < len(l2):
                if p1 < len(l1) and p2 < len(l2):
                    if l1[p1] < l2[p2]:
                        new_list.append(l1[p1])
                        p1 += 1
                    else:
                        new_list.append(l2[p2])
                        p2 += 1
                elif p1 < len(l1):
                    new_list += l1[p1:]
                    p1 = len(l1)
                else:
                    new_list += l2[p2:]
                    p2 = len(l2)
            return new_list
        if len(nums) <= 1:
            return nums
        pivot = len(nums) // 2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        return merge(left, right)
