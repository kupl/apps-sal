class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        key = {v: i for i, v in enumerate(req_skills)}
        dp = {0: tuple()}
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p:
                if skill in key:
                    his_skill |= 1 << key[skill]
            for skill_set, need in list(dict(dp).items()):
                with_him = skill_set | his_skill
                if with_him == skill_set: continue
                if with_him in dp and len(dp[with_him]) <= len(need) + 1: continue
                dp[with_him] = need + tuple([i])
        return dp[(1 << len(req_skills)) - 1]

