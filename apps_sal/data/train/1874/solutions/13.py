class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        N = max(answers)

        bincount = [0] * (N + 1)
        for a in answers:
            bincount[a] += 1

        min_number_rabbits = 0
        for i in range(N + 1):
            if bincount[i] == 0:
                continue
            group_size = i + 1
            nb_groups = math.ceil(bincount[i] / group_size)
            min_number_rabbits += nb_groups * group_size

        return min_number_rabbits
