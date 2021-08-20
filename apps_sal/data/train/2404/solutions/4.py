class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        target = 0
        if len(arr) == arr[-1]:
            target = k + arr[-1]
        else:
            for n in range(1, arr[-1] + 2):
                missing.append(n)
            for m in arr:
                missing.remove(m)
            if k > len(missing):
                target = missing[-1] + k - len(missing)
            else:
                target = missing[k - 1]
        return target
