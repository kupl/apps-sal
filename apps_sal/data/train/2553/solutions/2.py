class Solution:

    def numPrimeArrangements(self, n: int) -> int:
        p_nums = []
        c_nums = []
        dp = [True for _ in range(n + 1)]
        dp[0] = False
        dp[1] = False
        for i in range(2, n + 1):
            if dp[i] == True:
                cnt = 2
                while i * cnt < n + 1:
                    dp[i * cnt] = False
                    cnt += 1
        for i in range(1, n + 1):
            if dp[i]:
                p_nums += [i]
            else:
                c_nums += [i]
        return self.fact(len(p_nums) % (10 ** 9 + 7)) * self.fact(len(c_nums)) % (10 ** 9 + 7)

    def fact(self, n):
        if n <= 1:
            return 1
        else:
            return n * self.fact(n - 1)
    '\n    题目描述\n\n中文：质数排列\n英语：Prime Arrangements\n\n解题思路\n\n理解题意，是要求1到n的排列组合数，但并不是全排列，而是1到n中所有质数个数的阶乘和非质数个数的阶乘的乘积并对10^9 + 7即1000000007取模运算的结果。\n以n=5为例，1到5中有2、3、5共3个质数，非质数则有1、4共2个，则结果为(3! * 2!) % 1000000007 = 12\n\n代码如下\n\n需要理解的点 模运算规则：(a * b) % m = ((a % m) * b) % m 证明方法请自行搜索\n\n将数字分为质数和非质数两部分。\n假设有 p个质数，答案就是 p!⋅(n−p)!\n\n     '
