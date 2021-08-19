from collections import Counter


class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 9:
            return self.findMode(arr)
        c = [arr[0], arr[(n - 1) // 8], arr[2 * (n - 1) // 8], arr[3 * (n - 1) // 8], arr[4 * (n - 1) // 8], arr[5 * (n - 1) // 8], arr[6 * (n - 1) // 8], arr[7 * (n - 1) // 8], arr[n - 1]]
        return self.findMode(c)

    def findMode(self, arr: List[int]) -> int:
        return collections.Counter(arr).most_common(1)[0][0]
