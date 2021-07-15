class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = list(range(1,2001))
        res = list(set(res) - set(arr))
        print(res)
        return res[k-1]
