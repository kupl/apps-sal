class Solution:

    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ans = []
        for new in asteroids:
            while True:
                if ans and new < 0 < ans[-1]:
                    if ans[-1] < abs(new):
                        ans.pop()
                        continue
                    elif ans[-1] == abs(new):
                        ans.pop()
                    break
                else:
                    ans.append(new)
                    break
        return ans
