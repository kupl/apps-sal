class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        last = arr[-1]
        new = []
        for i in range(1, last):
            if i not in arr:
                new.append(i)
        if len(new) >= k:
            return new[k - 1]
        else:
            end = k - len(new)
            return last + end
