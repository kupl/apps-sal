class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        setter = set(arr)
        a_fourth = len(arr) / 4
        for elem in setter:
            if arr.count(elem) > a_fourth:
                return elem
