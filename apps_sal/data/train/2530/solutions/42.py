class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        songs_dict = [0] * 60
        res = 0
        for t in time:
            res += songs_dict[-t % 60]
            songs_dict[t % 60] += 1
        return res
