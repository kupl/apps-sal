class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dct = {}
        for num in arr:
            if num in dct:
                dct[num] += 1
            else:
                dct[num] = 1
        return len(list(dct.values())) == len(set(dct.values()))
