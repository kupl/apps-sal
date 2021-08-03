class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        sLen = len(stamp)
        tLen = len(target)
        dp = {}
        # buttom up DP approach

        def dfs(sidx, tidx, result):
            \"\"\"
            1. stamp[sidx] == target[tidx], sidx+=1, tidx+=1
            2. stamp[sidx] != target[tidx], dp[sidx, tidx] = []
            3. sidx == sLen, stamp is done, backtrace
            4. end criteria, tidx == tLen, and sidx == sLen (stamp要蓋完)

            using sidx, tidx as key for DP
            \"\"\"

            if tidx == tLen:
                dp[sidx, tidx] = result if sidx == sLen else []

            if (sidx, tidx) not in dp:
                if sidx == sLen:
                    # backtracking

                    for idx in range(sLen):
                        dp[sidx, tidx] = dfs(idx, tidx, [tidx-idx] + result)

                        if dp[sidx, tidx]:
                            break

                elif stamp[sidx] == target[tidx]:
                    nextResult = dfs(sidx+1, tidx+1, result)
                    dp[sidx, tidx] = nextResult if nextResult else dfs(0, tidx+1, result + [tidx+1])

                else:
                    dp[sidx, tidx] = []

            return dp[sidx, tidx]

        return dfs(0, 0, [0])

