class Solution:

    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0
        count = collections.Counter(answers)
        res = 0
        for (key, value) in count.items():
            if key == 0:
                res += count[0]
            elif key + 1 > value:
                res += key + 1
            elif value % (key + 1) == 0:
                res += value
            else:
                res += (key + 1) * (value // (key + 1) + 1)
        return res
