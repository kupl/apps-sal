class Solution:

    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        (st, res) = ([], [])
        for ast in asteroids:
            if ast > 0:
                st.append(ast)
                continue
            elif not st:
                res.append(ast)
                continue
            flag = True
            while st:
                if abs(ast) < st[-1]:
                    flag = False
                    break
                ast1 = st.pop()
                if abs(ast) == ast1:
                    flag = False
                    break
            if flag:
                res.append(ast)
        return res + st
