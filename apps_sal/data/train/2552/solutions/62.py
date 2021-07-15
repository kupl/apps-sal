class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l = len(arr)
        bound = l/4
        s = set()
        for i in arr:
            if i not in s:
                if arr.count(i)>bound:
                    return i
                s.add(i)
