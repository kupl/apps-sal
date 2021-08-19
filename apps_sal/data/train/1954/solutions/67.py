class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dic = {v: i for (i, v) in enumerate(req_skills)}
        dp = dict()
        for (i, people_skill) in enumerate(people):
            skill = 0
            for single_skill in people_skill:
                skill |= 1 << dic[single_skill]
            dp[skill] = [i]
            for (key, value) in list(dp.items()):
                if key != skill:
                    new_skill = key | skill
                    if new_skill not in list(dp.keys()) or len(dp[new_skill]) > len(dp[key]) + 1:
                        dp[new_skill] = dp[key] + [i]
        return dp[(1 << len(req_skills)) - 1]
