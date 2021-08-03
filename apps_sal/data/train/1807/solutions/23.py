class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        l = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if math.gcd(i, j) < 2:
                    l += [f'{j}/{i}']
        return l

#         def memoize(f):
#             memo = {}
#             def helper(x):
#                 if x not in memo:
#                     memo[x] = f(x)
#                 return memo[x]
#             return helper

#         def hcf(a, b):
#             for i in range(2, a+1):
#                 if a % i == 0 and b % i == 0:
#                     return False
#             return True

#         def cal(x):
#             l = []
#             for i in range(1, x):
#                 if hcf(i, x):
#                     l += [\"{}/{}\".format(i, x)]
#             return l

#         def fib(n):
#             if n == 1:
#                 return []
#             elif n == 2:
#                 return [\"1/2\"]
#             else:
#                 return fib(n-1) + cal(n)


#         fib = memoize(fib)

#         return fib(n)
