class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        key = {v: k for (k, v) in enumerate(req_skills)}
        dp = {0: []}
        for (i, skills) in enumerate(people):
            person_skill = 0
            for skill in skills:
                person_skill |= 1 << key[skill]
            for (skill_set, need) in list(dict(dp).items()):
                nxt_skill_set = skill_set | person_skill
                if nxt_skill_set == skill_set:
                    continue
                if nxt_skill_set in dp and len(dp[nxt_skill_set]) <= len(need) + 1:
                    continue
                dp[nxt_skill_set] = need + [i]
        return dp[(1 << len(req_skills)) - 1]
