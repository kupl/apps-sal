class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A)

        freq = {}
        maxv = (None, -math.inf)
        for v in A:
            if v not in freq:
                freq[v] = 0
            freq[v] += 1
            if freq[v] > maxv[1]:
                maxv = (v, freq[v])
            if freq[v] == N:
                return v

        return maxv[0]
