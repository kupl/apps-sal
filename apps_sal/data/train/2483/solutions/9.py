class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}

        for i in arr:
            counter[i] = counter.get(i, 0) + 1

        return len(counter.values()) == len(set(list(counter.values())))
