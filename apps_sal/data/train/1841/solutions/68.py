class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        x = sorted(arr)
        l = len(arr)

        median = x[(l - 1) // 2]
        jj = sorted(list(range(len(arr))), key=lambda y: (abs(arr[y] - median), arr[y]), reverse=True)
        n = [arr[i] for i in jj]
        return n[:k]
