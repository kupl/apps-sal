class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        arrlen = len(arr)
        arrcnt = Counter(arr)
        for (key, val) in arrcnt.items():
            if val * 4 > arrlen:
                return key
