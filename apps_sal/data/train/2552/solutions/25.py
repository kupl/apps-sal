class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        condensed = set(arr)
        counter = 0
        digit = 0
        print(condensed)
        for i in condensed:
            temp = arr.count(i)
            if counter < temp:
                counter = temp
                digit = i
        return digit
