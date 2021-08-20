class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        target = (1 << n) - 1
        dic = {x: index for (index, x) in enumerate(req_skills)}
        skillsMap = []
        for i in people:
            mask = 0
            for sk in i:
                mask |= 1 << dic[sk]
            skillsMap.append(mask)
        dp = [float('inf')] * (1 << n)
        par = [(0, 0)] * (1 << n)
        dp[0] = 0
        for (i, k) in enumerate(skillsMap):
            if k != 0:
                for j in range(target, -1, -1):
                    if dp[j] + 1 < dp[j | k]:
                        dp[j | k] = dp[j] + 1
                        par[j | k] = (j, i)
        res = []
        while target:
            res.append(par[target][1])
            target = par[target][0]
        return res
