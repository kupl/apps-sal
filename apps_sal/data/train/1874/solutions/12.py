class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if answers == []:
            return 0
        d = {}
        for n in answers:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        total = 0
        for n in d:
            if d[n] % (n + 1) == 0:
                total += d[n]
            else:
                total += ((d[n] // (n + 1)) + 1) * (n + 1)

        return total
