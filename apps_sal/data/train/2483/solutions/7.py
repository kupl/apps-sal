class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        count_dict = dict(Counter(arr))
        count_occurrences = [j for (i, j) in list(count_dict.items())]
        return len(set(arr)) == len(set(count_occurrences))
