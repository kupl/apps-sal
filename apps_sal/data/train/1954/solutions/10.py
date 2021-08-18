class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        d = dict()
        for i in range(n):
            d[req_skills[i]] = i
        dp = [list(range(len(people))) for _ in range(1 << n)]
        dp[0] = []
        for i in range(len(people)):
            skill = 0
            for s in people[i]:
                skill |= (1 << d[s])
            for k, v in enumerate(dp):
                new_skills = k | skill
                if new_skills != k and len(dp[new_skills]) > len(v) + 1:
                    dp[new_skills] = v + [i]
        return dp[(1 << n) - 1]
