class Solution:
    #Version 1: DP
    #left[i][j] is the longest 1 on the right hand side ending at mat[i][j]
    #up[i][j] is the longest 1 above mat[i][j]
    #TC: O(mnn), SC: O(mn)
    '''
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        left = [[0]*n for _ in range(m)]
        up = [[0]*n for _ in range(m)]
        
        for k in range(m):
            count = 0
            for v in range(n):
                if mat[k][v] == 1:
                    count += 1
                else:
                    count = 0
                left[k][v] = count
                    
        for v in range(n):
            count = 0
            for k in range(m):
                if mat[k][v] == 1:
                    count += 1
                else:
                    count = 0
                up[k][v] = count
            
        ans = 0
        for k in range(m):
            for v in range(n):
                if mat[k][v] == 1:
                    current = up[k][v]
                    for j in range(left[k][v]):
                        current = min(current, up[k][v-j])
                        ans += current
                    #print(k, v, ans, left[k][v], right[k][v], up[k][v], down[k][v])
        return ans
    '''
    
    #Version 2: Stack and dp
    #Consider the histogram in the first m rows
    #dp[k] stores the the number of submatrices using mat[m][k] as the right bottom
    #We can use stack to consider the case, once we found there is a index h[i] <= h[v], the result will be dp[v] = dp[i] + (v-i)*h[v]
    #TC: O(mn), SC: O(n)
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ans = 0
        h = [0]*n
        for k in range(m):
            for v in range(n):
                if mat[k][v] == 1:
                    h[v] += 1
                else:
                    h[v] = 0

            dp = [0]*n
            # stack = []
            # for v in range(n):
            #     while stack and h[stack[-1]] >= h[v]:
            #         stack.pop()
            #     if not stack:
            #         dp[v] = h[v] * (v+1)
            #     else:
            #         dp[v] = dp[stack[-1]] + (v - stack[-1])*h[v]
            #     stack.append(v)
            #     ans += dp[v]
            dp = [0]*(n+1)
            stack = [[-1, 0]]
            for v in range(n):
                while stack and stack[-1][0] >= h[v]:
                    stack.pop()
                dp[v+1] = dp[stack[-1][1]] + (v + 1 - stack[-1][1])*h[v]
                stack.append([h[v], v+1])
                ans += dp[v+1]
            #print(k, h, dp)
        return ans
    

