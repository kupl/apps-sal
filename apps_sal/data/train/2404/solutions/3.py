class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        if len(arr) == 0:
            return k
        i = 1
        s = set(arr)
        while True:
            if i not in s:
                k -= 1
                if k == 0:
                    return i
            i += 1
        return -1
