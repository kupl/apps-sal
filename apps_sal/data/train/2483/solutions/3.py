class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = {}
        check = set()
        for num in arr:
            if num not in occur:
                occur[num] = arr.count(num)
        for num in occur.values():
            check.add(num)
        if len(occur) == len(check):
            return True
        return False
