import numpy

# bruteforce
def gobf(piles, i, m, alex):
    res = 0 if alex == 1 else float(\"inf\")
    if i == len(piles):
        return 0
        
    for x in range(1, 2 * m + 1):
        if i + x > len(piles):
            break
        if alex == 1:
            res = max(res, sum(piles[i:i+x]) + gobf(piles, i+x, max(x,m), 0))
        else:
            res = min(res, gobf(piles, i+x, max(x,m), 1))
    return res


# memo
def go(piles, i, m, alex, memo):
    if i == len(piles):
        return 0
    if memo[i][m][alex] != -1:
        return memo[i][m][alex]
        
    res = 0 if alex == 1 else float(\"inf\")
    for x in range(1, 2 * m + 1):
        if i + x > len(piles):
            break
        if alex == 1:
            res = max(res, sum(piles[i:i+x]) + go(piles, i+x, max(x,m), 0, memo))
        else:
            res = min(res, go(piles, i+x, max(x,m), 1, memo))
    memo[i][m][alex] = res
    return memo[i][m][alex]

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = numpy.ndarray((n, n + 1, 2), int)
        memo.fill(-1)
        return go(piles, 0, 1, 1, memo)
