class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maximum = 0
        count = Counter(arr)
        
        for key,value in count.items():
            if key == value:
                if value > maximum:
                    maximum = value
        if maximum != 0:
            return maximum
        
        return -1
