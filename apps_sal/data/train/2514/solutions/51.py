class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        cnt = 0
        ans = 0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) > d:
                    cnt += 1
                else:
                    cnt = 0
                    break
                if j == len(arr2) - 1 and cnt == len(arr2):
                    ans += 1
                    cnt = 0

        return ans
