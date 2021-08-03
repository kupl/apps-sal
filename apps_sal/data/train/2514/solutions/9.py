class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n, m = len(arr1), len(arr2)
        ans = 0
        for i in range(n):
            flag = 0
            for j in range(m):
                if abs(arr1[i] - arr2[j]) <= d:
                    flag = 1
            if not flag:
                ans += 1
        return ans
