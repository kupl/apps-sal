class Solution:

    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0
        rabbits = 0
        answers = sorted(answers)
        n = len(answers)
        not_count = 0
        iteration = 1
        prev_value = 0
        for i in range(n):
            if iteration >= not_count or prev_value != answers[i]:
                rabbits += answers[i] + 1
                iteration = 0
                not_count = answers[i] + 1
                prev_value = answers[i]
            iteration += 1
        return rabbits
