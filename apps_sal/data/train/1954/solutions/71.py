class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        m = len(people)
        key = {v: i for (i, v) in enumerate(req_skills)}
        dp = {0: []}
        for (i, p) in enumerate(people):
            his_skill = 0
            for skill in p:
                his_skill |= 1 << key[skill]
            if his_skill == 0:
                continue
            for (skill_set, need) in list(dp.items()):
                with_him = skill_set | his_skill
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]
