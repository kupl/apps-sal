class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        num_dict = {}
        for num in arr:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        return max(num_dict, key=lambda k: num_dict[k])
