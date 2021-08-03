class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        unique = Counter(time)
        time = list(set(time))

        for i in range(len(time)):
            if unique[time[i]] > 1:
                if 2 * time[i] % 60 == 0:
                    res += math.factorial(unique[time[i]]) // (2 * math.factorial(unique[time[i]] - 2))
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    res += unique[time[j]] * unique[time[i]]
        return res
