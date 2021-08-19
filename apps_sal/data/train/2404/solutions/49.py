class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        vec = []
        numbers = [x + 1 for x in range(max(arr) + k)]
        for x in numbers:
            if x not in arr:
                vec.append(x)
        return vec[k - 1]
