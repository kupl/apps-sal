class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def f(n):
            if n == 0: return [0]
            else:
                return f(n-1) + [2**(n-1) + v for v in f(n-1)[::-1]]
        res = f(n)
        i = res.index(start)
        return res[i:] + res[:i]
        

