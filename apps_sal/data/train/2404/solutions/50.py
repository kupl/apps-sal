class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = []
        x = 1
        for i in range(k+max(arr)):
            if x not in arr:
                l.append(x)
                x += 1
            else:
                x += 1
        return l[k-1]
