class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        the_dict = {}
        for num in arr:
            the_dict[num] = the_dict.get(num, 0) + 1
        
        for item in list(the_dict.items()):
            if item[1] == max(the_dict.values()):
                return item[0]
