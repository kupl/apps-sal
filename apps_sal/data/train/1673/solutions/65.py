class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        memo = {}
        return self.helper(0, None, arr, memo)

    def helper(self, index, notAllowed, arr, memo):
        if (index == len(arr)):
            return 0
        elif (index, notAllowed) in memo:
            return memo[(index, notAllowed)]
        else:
            maxOne, maxTwo = self.getMaxTwo(notAllowed, arr[index])
            useOne = arr[index][maxOne] + self.helper(index + 1, maxOne, arr, memo)
            useTwo = arr[index][maxTwo] + self.helper(index + 1, maxTwo, arr, memo)
            res = min(useOne, useTwo)
            memo[(index, notAllowed)] = res
            return res

    def getMaxTwo(self, blocked, arr):
        minOne = None
        minIndex = None
        for i in range(len(arr)):
            if (i == blocked):
                continue
            else:
                curr_num = arr[i]
                if (minOne == None) or (curr_num < minOne):
                    minOne = curr_num
                    minIndex = i
        minTwo = None
        minIndexTwo = None
        for j in range(len(arr)):
            if (j == blocked) or (j == minIndex):
                continue
            else:
                curr_num = arr[j]
                if (minTwo == None) or (curr_num < minTwo):
                    minTwo = curr_num
                    minIndexTwo = j
        return minIndex, minIndexTwo
