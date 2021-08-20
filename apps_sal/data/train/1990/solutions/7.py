class Solution(object):

    def findLongestChain(self, pairs):
        pairs = sorted(pairs, key=lambda x: x[1])
        count = 1
        curr = pairs[0]
        for pair in pairs:
            if curr[1] < pair[0]:
                count += 1
                curr = pair
        return count
