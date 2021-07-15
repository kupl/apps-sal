class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skillIdx = {}
        dp = {}
        dp[0] = []
        
        for idx, skill in enumerate(req_skills):
            skillIdx[skill] = idx
        
        for idx, personSkills in enumerate(people):
            skillBits = 0
            for skill in personSkills:
                skillBits |= 1 << skillIdx[skill]
            for prevSkills, _ in list(dp.items()):
                newSkills = prevSkills | skillBits
                if newSkills == prevSkills:
                    continue
                if newSkills not in dp or len(dp[newSkills]) > len(dp[prevSkills]) + 1:
                    dp[newSkills] = dp[prevSkills] + [idx]
        
        return dp[(1 << len(req_skills)) - 1]

