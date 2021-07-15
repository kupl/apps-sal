from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return [key for key, value in Counter(arr).items() if value > len(arr) // 4][0]
