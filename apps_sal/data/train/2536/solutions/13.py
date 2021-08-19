class Solution:

    def findLucky(self, arr: List[int]) -> int:
        max1 = -1
        n = len(arr)
        for i in range(n):
            flag = False
            count = 0
            for j in reversed(range(0, i)):
                if arr[i] == arr[j]:
                    flag = True
                    break
            if flag == True:
                continue
            for j in range(i, n):
                if arr[j] == arr[i]:
                    count += 1
            if arr[i] == count:
                if max1 < arr[i]:
                    max1 = arr[i]
        return max1
