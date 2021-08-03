class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        integer = list(range(1, max(arr) + k + 1))
        result = []
        while(len(result) < k):
            for i in integer:
                if i not in arr:
                    result.append(i)
        return result[k - 1]
