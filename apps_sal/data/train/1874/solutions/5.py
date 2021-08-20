class Solution:

    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        answers.sort()
        answers_len = len(answers)
        result = 0
        index = 0
        while True:
            if index >= answers_len:
                break
            if answers[index] == 0:
                result += 1
                index += 1
                if index >= answers_len:
                    break
            else:
                result += answers[index] + 1
                this_answer = answers[index]
                index += 1
                if index >= answers_len:
                    break
                for _ in range(this_answer):
                    if answers[index] == this_answer:
                        index += 1
                        if index >= answers_len:
                            break
        return result
