def gcd(x, y):
    # while y != 0:
    #     (x, y) = (y, x%y)
    # return x
    if y == 0:
        return x
    else: 
        return gcd(y, x%y)

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            for j in range(i, n+1):
                if i == j: continue
                if gcd(i,j) == 1:
                    ans.append(str(i) + \"/\" + str(j))
        return ans
