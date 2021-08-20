import heapq


class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        heatMap = [0 for i in range(len(nums) + 1)]
        for req in requests:
            heatMap[req[0]] += 1
            heatMap[req[1] + 1] -= 1
        for i in range(1, len(heatMap)):
            heatMap[i] += heatMap[i - 1]
        heatMap.sort(reverse=True)
        nums.sort(reverse=True)
        numIndex = 0
        total = 0
        for count in heatMap:
            if count == 0:
                break
            total += nums[numIndex] * count
            numIndex += 1
        return total % (10 ** 9 + 7)
