class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a2 = arr.copy()
        arr.extend([i for i in range(arr[-1] + 1, arr[-1] + 1 + k)])
        print(a2)
        for i in range(1, a2[-1] + 1):
            if i not in arr:
                k -= 1
            if k == 0:
                return i
        return a2[-1] + k
