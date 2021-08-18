class Solution:
    def validMountainArray(self, A: List[int]) -> bool:

        if len(A) < 3:
            return False

        diffs = [A[i + 1] - A[i] for i in range(len(A) - 1)]

        if 0 in diffs or diffs[0] < 0:
            return False

        peak = False
        for i in range(len(diffs) - 1):
            if diffs[i + 1] / abs(diffs[i + 1]) != diffs[i] / abs(diffs[i]):
                if peak == False:
                    peak = True
                else:
                    return False
        return peak
