class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n_miss = 0
        i = 0
        c = 1
        n = len(arr)
        while n_miss < k:
            if i < n and arr[i] == c:
                c += 1
                i += 1
            else:
                c += 1
                n_miss += 1
        return c - 1
