class Solution:

    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        return sum((count + -count % (i + 1) for (i, count) in collections.Counter(answers).items()))
