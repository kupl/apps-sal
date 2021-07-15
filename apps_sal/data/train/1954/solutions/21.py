class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        n, m = len(req_skills), len(people)
        key = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p: his_skill |= 1 << key[skill]
            if his_skill == 0 or his_skill in dp and len(dp[his_skill]) == 1: continue
            sn = copy.deepcopy(list(dp.items()))
            for skill_set, need in sn:
                with_him = skill_set | his_skill
                if with_him == skill_set: continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]
