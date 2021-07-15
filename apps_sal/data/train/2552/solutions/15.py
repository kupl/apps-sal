class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        unique_nums = list(dict.fromkeys(arr))
        
        for unique_num in unique_nums:
            if (arr.count(unique_num) / len(arr)) > 0.25:
                return unique_num

