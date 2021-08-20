class Solution:

    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        rabbit = {}
        for n in set(answers):
            rabbit[n] = answers.count(n)
        res = 0
        for i in rabbit.keys():
            res += math.ceil(rabbit[i] / (i + 1)) * (i + 1)
        return res
