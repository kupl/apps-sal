class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        for i, ai in enumerate(arr):
            for k, ak in enumerate(arr[i+2:], i+2):
                if abs(ak-ai) <= c:
                    for j, aj in enumerate(arr[i+1:k], i+1):
                        if abs(ai-aj) <= a and abs(ak-aj) <= b:
                            res += 1
        return res
