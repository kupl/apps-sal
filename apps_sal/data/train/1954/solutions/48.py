class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dp = {0: []}
        reqSkills = {v: k for (k, v) in enumerate(req_skills)}
        for (i, curSkills) in enumerate(people):
            curMask = 0
            for skill in curSkills:
                curMask |= 1 << reqSkills[skill]
            for (mask, team) in list(dp.items()):
                m = mask | curMask
                if m == mask:
                    continue
                if m not in dp or 1 + len(team) < len(dp[m]):
                    dp[m] = team + [i]
        return dp[(1 << len(req_skills)) - 1]
