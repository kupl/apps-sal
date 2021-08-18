class Solution:
    def findLucky(self, arr: List[int]) -> int:

        dict = {}
        ans = -1
        for x in range(len(arr)):
            if arr[x] not in dict:
                dict[arr[x]] = 1
            else:
                dict[arr[x]] += 1
        for key, value in dict.items():
            if key == value:
                ans = max(ans, key)
        return ans
