class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 1
        while k > 0:
            if count not in arr:
                k = k - 1
                print(k)
            count += 1
        return count - 1
