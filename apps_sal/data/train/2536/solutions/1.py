from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        lucky = [element for element, frequency in list(count.items())if element == frequency]
        return max(lucky) if lucky else -1
