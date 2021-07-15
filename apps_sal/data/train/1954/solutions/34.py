class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = {val: i for i, val in enumerate(req_skills)}
        n = len(req_skills)
        skills = [reduce(lambda a, b: a + b, [1 << m[s] for s in row] or [0]) for row in people]
        final_state = reduce(lambda a, b: a + b, [1 << i for i in range(n)])
        dp = {0: []}
        for i, skill in enumerate(skills):
            for prev_state, team in dp.copy().items():
                new_state = prev_state | skill
                if new_state == prev_state: continue
                if new_state not in dp or len(team) + 1 < len(dp[new_state]):
                    dp[new_state] = team + [i]
        
        return dp[final_state] 
