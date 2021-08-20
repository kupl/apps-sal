class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        (n, m) = (len(req_skills), len(people))
        dic = {v: i for (i, v) in enumerate(req_skills)}
        dp = {0: []}
        for (i, p) in enumerate(people):
            cur_skill = 0
            for s in p:
                if s in dic:
                    cur_skill |= 1 << dic[s]
            for (skill_set, team) in list(dp.items()):
                new_skill = skill_set | cur_skill
                if new_skill != skill_set:
                    if new_skill not in dp or len(team) + 1 < len(dp[new_skill]):
                        dp[new_skill] = team + [i]
        return dp[(1 << n) - 1]
