class Solution:
    def numRabbits(self, answers):
        cnts = collections.Counter(answers)
        return sum(-v % (k + 1) + v for k, v in cnts.items())
