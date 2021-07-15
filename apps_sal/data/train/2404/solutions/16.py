class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if not arr:
            return k

        last = arr[-1]
        for i in range(last):
            if i not in arr:
                if k == 0:
                    return i
                k -= 1


        while k:
            last += 1
            k -= 1

        return last + 1
