"""
We know that any given substring must be such that for all digits in substring, at most one of those has odd frequency. So, we probably need to find a clever way to figure out the longest such string with that propery.
It seems like we can do something where we go from largest ending in index i to largest ending in index i+1 where we use fact if character a doesn't change the above constraints, then that is obvious answer. Otherwise, we would then have to remove stuff from early on in string tied to index i until we are valid.
"""


class Solution:

    def longestAwesome(self, s: str) -> int:
        sLength = len(s)
        earliestBinaries = {}
        current = [0] * 10
        earliestBinaries[tuple(current)] = -1
        currentMax = 0

        def computeMaxFromNeighbors(counter, currentTuple):
            currentMax = 0
            if currentTuple in earliestBinaries:
                currentMax = max(currentMax, counter - earliestBinaries[currentTuple])
            neighborList = list(currentTuple)
            for i in range(len(currentTuple)):
                neighborList[i] = 1 - neighborList[i]
                neighborTuple = tuple(neighborList)
                if neighborTuple in earliestBinaries:
                    currentMax = max(currentMax, counter - earliestBinaries[neighborTuple])
                neighborList[i] = 1 - neighborList[i]
            return currentMax
        for (counter, char) in enumerate(s):
            current[int(char)] = 1 - current[int(char)]
            currentTuple = tuple(current)
            currentMax = max(currentMax, computeMaxFromNeighbors(counter, currentTuple))
            if currentTuple not in earliestBinaries:
                earliestBinaries[currentTuple] = counter
        return currentMax
