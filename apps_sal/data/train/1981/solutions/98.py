class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        def getFreq():
            minVal = sys.maxsize
            maxVal = 0
            freq = [0 for _ in range(len(nums) + 1)]
            for i in range(len(requests)):
                low = requests[i][0]
                freq[low] = freq[low] + 1
                high = requests[i][1]
                freq[high + 1] = freq[high + 1] - 1
                if low < minVal:
                    minVal = low
                if high > maxVal:
                    maxVal = high
            for i in range(minVal + 1, maxVal + 2):
                freq[i] = freq[i] + freq[i - 1]
            return freq[:-1]
        answer = 0
        freq = getFreq()
        freq = sorted(freq)
        nums = sorted(nums)
        for i in range(1, len(nums) + 1):
            answer = (answer + freq[i - 1] * nums[i - 1]) % (10 ** 9 + 7)
        return answer
