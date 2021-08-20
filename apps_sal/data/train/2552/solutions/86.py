class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = Counter(arr)
        return [k for (k, v) in dic.items() if v == max(dic.values())][0]
