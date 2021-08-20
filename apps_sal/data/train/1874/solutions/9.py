class Solution:

    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        total = 0
        d = collections.defaultdict(int)
        for ans in answers:
            d[ans] += 1
        for (k, v) in d.items():
            total += math.ceil(v / (k + 1)) * (k + 1)
        return total
