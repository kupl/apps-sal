class Solution:

    def findTheDistanceValue(self, arr1, arr2, d):
        d = abs(d)
        res = 0
        for i in range(len(arr1)):
            count = 0
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    break
                else:
                    count += 1
                if count == len(arr2):
                    res += 1
        return res


sol = Solution()
x = sol.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2)
print(x)
