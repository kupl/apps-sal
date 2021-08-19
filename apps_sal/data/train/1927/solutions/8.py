class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            if a >= 0 or a < 0 and (not stack or stack[-1] < 0):
                stack.append(a)
            else:
                while a < 0 and stack and stack[-1] > 0:
                    last = stack.pop()  # last > 0
                    a = a if -a > last else last if -a < last else 0
                if a != 0:
                    stack.append(a)

        return stack
