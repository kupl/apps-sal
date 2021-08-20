class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        freq = list(c.values())
        return len(freq) == len(set(freq))
