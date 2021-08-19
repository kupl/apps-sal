class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        frequency = [0 for i in range(len(nums))]
        for request in requests:
            (start, end) = request
            frequency[start] += 1
            if end + 1 < len(frequency):
                frequency[end + 1] -= 1
        indexToFrequency = []
        for i in range(0, len(frequency)):
            if i != 0:
                frequency[i] += frequency[i - 1]
            indexToFrequency.append((frequency[i], i))
        indexToFrequency.sort(reverse=True)
        nums.sort(reverse=True)
        numbers = [0 for _ in range(len(nums))]
        for i in range(len(indexToFrequency)):
            (_, index) = indexToFrequency[i]
            numbers[index] = nums[i]
        prefixSum = list(numbers)
        for i in range(1, len(numbers)):
            prefixSum[i] += prefixSum[i - 1]
            prefixSum[i] %= 10 ** 9 + 7
        result = 0
        for request in requests:
            (start, end) = request
            if start == 0:
                result += prefixSum[end]
            else:
                result += prefixSum[end] - prefixSum[start - 1]
            result = result % (10 ** 9 + 7)
        return result
