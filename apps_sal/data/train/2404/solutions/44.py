class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        standard = []
        for i in range(1, arr[-1] + k + 1):
            standard.append(i)

        diff = []
        for i in standard:
            if i not in arr:
                diff.append(i)

        return diff[k - 1]
