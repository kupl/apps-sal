class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        hm = {v:i for i, v in enumerate(req_skills)}
        dp = {0:[]}
        
        for i, skills in enumerate(people):
            p_skills = 0
            for sk in skills:
                if sk in hm:
                    p_skills |= 1<<(hm[sk])
                    
            for sks, need in list(dp.items()):
                now = sks|p_skills
                
                if now not in dp or len(dp[now])>len(need)+1:
                    dp[now] = need+[i]
                    
        return dp[(1<<len(req_skills))-1]

