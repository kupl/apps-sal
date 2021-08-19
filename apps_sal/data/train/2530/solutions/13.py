class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # in a list of songs, the ith song has a duration of time[i] seconds
        # return number of pairs of songs for which their total duration in seconds is divisible by 60 seconds
        # O(n^2) solution
        # nested for loops

        # initialize pairs = 0
        table = defaultdict(int)
        c = 0
        for i, t in enumerate(time):
            if (60 - (t % 60)) % 60 in table:
                c += table[(60 - (t % 60)) % 60]
            table[(t % 60)] += 1
        return c
