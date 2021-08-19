class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 递归超时。。
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1)+self.climbStairs(n-2)

        # 改进递归，使用cache
        cache = {}

        def f(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in list(cache.keys()):
                return cache[n]
            cache[n] = f(n - 1) + f(n - 2)
            return cache[n]
        return f(n)

        # 改成循环。递推公式为。f(n) = f(n-1) + f(n-2)
