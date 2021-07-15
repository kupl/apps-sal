class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) / 4
        count = 0
        temp = []
        
        for item in arr:
            if item not in temp:
                temp.append(item)
        
        for item in temp:
            count = arr.count(item)
            if count > quarter:
                return item
