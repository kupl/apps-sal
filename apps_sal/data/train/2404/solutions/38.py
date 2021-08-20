class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        x = []
        for i in range(1, 1000):
            while len(x) <= k:
                if i not in arr:
                    x.append(i)
                i = i + 1
        print(x)
        return x[k - 1]
