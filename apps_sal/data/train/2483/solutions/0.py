from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = defaultdict(int)
        for i in arr:
            occurences[i] += 1
        for i in occurences.values():
            if list(occurences.values()).count(i) > 1:
                return False
        return True
