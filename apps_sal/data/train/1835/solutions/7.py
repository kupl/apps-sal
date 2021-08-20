class Solution:

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        def solve(x):
            s = str(x)
            if len(s) > 1 and abs(int(s[-1]) - int(s[-2])) != k:
                return
            if len(s) == n and abs(int(s[-1]) - int(s[-2])) == k:
                result.append(x)
            if len(s) == n:
                return
            for i in range(0, 10):
                solve(x * 10 + i)
        result = []
        for i in range(1, 10):
            solve(i)
        return result
