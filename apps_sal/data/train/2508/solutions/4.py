class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        maxVal = max(heights)

        freq = [0] * (maxVal + 1)
        for num in heights:
            freq[num] += 1
        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]

        places = [0] * len(heights)
        for num in heights:
            places[freq[num] - 1] = num
            freq[num] -= 1

        ans = 0
        for i in range(len(heights)):
            if heights[i] != places[i]:
                ans += 1
        return ans
