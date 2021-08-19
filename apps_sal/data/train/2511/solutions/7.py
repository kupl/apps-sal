class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A)

        freq = {}
        maxv = (None, -math.inf)
        for v in A:
            # Initialize the map entry if v is not in the map
            if v not in freq:
                freq[v] = 0
            # Increment the frequency of v
            freq[v] += 1
            # Check if v is the maxmimum frequency element
            if freq[v] > maxv[1]:
                maxv = (v, freq[v])
            # Check if we're done
            if freq[v] == N:
                return v

        return maxv[0]
