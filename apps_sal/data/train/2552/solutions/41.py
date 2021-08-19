class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        d = Counter(arr)
        d = sorted(list(d.items()), key=lambda x: x[1], reverse=True)
        return d[0][0]
