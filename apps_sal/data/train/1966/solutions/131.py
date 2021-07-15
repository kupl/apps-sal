class Solution:
    def numSubmat(self, A: List[List[int]]) -> int:
        r = len(A)
        c = len(A[0])
        dp = [[0]*(c+1) for _ in range(r+1)]
        for i in range(r):
            dp[i][0] = 0
            for j in range(c):
                dp[i][j+1] = dp[i][j] + A[i][j]
        ans = 0
        for lhs in range(c):
            for rhs in range(lhs, c):
                amt = 0
                for i in range(r):
                    if dp[i][rhs+1] - dp[i][lhs] == rhs-lhs+1:
                        amt += 1 
                    else:
                        amt = 0
                    ans += amt
        return ans
        
        
        
\"\"\"
For each row i, create an array nums where:

mat[i][j] == 0 then nums[j] = 0 else nums[j] = nums[j-1] + 1

In row i, the number of rectangles between column j and k(inclusive) and ends in row i
is equal to sum(min(nums[j,...,idx])) where idx go from j to k


in row i the number of rectangles between column j and k that ends in row i is equal to
sum ( min ( row[j:idx+1])) for idx in range(j, k)

expected solution is O(n*3)
\"\"\"
