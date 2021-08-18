class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        target = (1 << n) - 1
        s_i = {s: i for i, s in enumerate(req_skills)}
        dp = {0: []}
        for j, row in enumerate(people):
            mask = 0
            new_dp = dp.copy()
            for s in row:
                mask |= (1 << s_i[s])
            for curr, cost in dp.items():
                new_mask = curr | mask
                if new_mask not in new_dp:
                    new_dp[new_mask] = cost + [j]
                else:
                    new_dp[new_mask] = min(new_dp[new_mask], cost + [j], key=len)
            dp = new_dp
        return dp[target]
