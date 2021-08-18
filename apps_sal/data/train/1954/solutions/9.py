class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        N, skill_dict = len(req_skills), {}
        for i in range(N):
            skill_dict[req_skills[i]] = i
        dp = [list(range(len(people))) for _ in range(1 << N)]
        dp[0] = []

        for i in range(len(people)):
            skill = 0
            for s in people[i]:
                skill |= (1 << skill_dict[s])

            for k, v in enumerate(dp):
                new_skill = k | skill
                if new_skill != k and len(v) + 1 < len(dp[new_skill]):
                    dp[new_skill] = v + [i]

        return dp[(1 << N) - 1]
