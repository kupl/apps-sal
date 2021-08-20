class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.partition(nums)

    def partition(self, num_list):
        if not num_list or len(num_list) == 1:
            return num_list
        pivot = num_list[0]
        left = []
        right = []
        for i in range(1, len(num_list)):
            if num_list[i] >= pivot:
                right.append(num_list[i])
            else:
                left.append(num_list[i])
        return self.partition(left) + [pivot] + self.partition(right)
