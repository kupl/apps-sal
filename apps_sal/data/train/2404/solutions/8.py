class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        x = [i for i in range(1, arr[-1] + 1)]
        for i in arr:
            if i in x:
                x.remove(i)
        for i in range(k):
            x.append(arr[-1] + i + 1)
        return x[k - 1]
