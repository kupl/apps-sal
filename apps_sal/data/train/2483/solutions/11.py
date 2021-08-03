class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        rec = [arr.count(elem) for elem in set(arr)]
        return len(rec) == len(set(rec))
