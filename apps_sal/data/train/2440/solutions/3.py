class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [0, 1, 2]
        if n < 3:
            return steps[n]
        for i in range(3, n + 1):
            steps.append(steps[i - 1] + steps[i - 2])
        return steps[n]
