class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        answers = sorted(answers)
        j = 0
        sum = 0
        while (answers[0] == 0):
            answers.pop(0)
            sum = sum + 1

        size = len(answers)

        while(j < size):
            val = answers[j]
            inc = 0
            while (j < size and val == answers[j] and inc < val + 1):
                inc = inc + 1
                j = j + 1
            sum = sum + val + 1

        return sum
