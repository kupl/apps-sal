class Solution:

    def heightChecker(self, heights: List[int]) -> int:
        max_val = max(heights)
        freq = [0] * (max_val + 1)
        for num in heights:
            freq[num] += 1
        for num in range(1, len(freq)):
            freq[num] += freq[num - 1]
        places = [0] * len(heights)
        for num in heights:
            places[freq[num] - 1] = num
            freq[num] -= 1
        return sum((a != b for (a, b) in zip(places, heights)))
