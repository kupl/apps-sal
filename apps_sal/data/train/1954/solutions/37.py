class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        dic = {x: i for i, x in enumerate(req_skills)}
        dp = {0:[]}
        for i, p in enumerate(people):
            his = 0
            for skill in p:
                his |= (1 << dic[skill])
            for s in list(dp.keys()):
                new = his | s
                if new == s:
                    continue
                if new not in dp or len(dp[new]) > len(dp[s]) + 1:
                    dp[new] = dp[s] + [i]
        return dp[(1 << len(req_skills)) - 1]
