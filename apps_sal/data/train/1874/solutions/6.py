class Solution:

    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        countArr = {}
        for i in answers:
            if i not in countArr.keys():
                countArr[i] = 1
            else:
                countArr[i] += 1
        minColors = 0
        for i in countArr.keys():
            minColors += math.ceil(countArr[i] / (i + 1)) * (i + 1)
        return minColors
