class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        (n, m) = (len(req_skills), len(people))
        key = {v: i for (i, v) in enumerate(req_skills)}
        dp = [[]] + [None] * ((1 << n) - 1)
        for (i, p) in enumerate(people):
            his_skill = 0
            for skill in p:
                if skill in key:
                    his_skill |= 1 << key[skill]
            for k in range(len(dp) - 1, -1, -1):
                with_him = k | his_skill
                if with_him == k or dp[k] is None:
                    continue
                if not dp[with_him] or len(dp[k]) + 1 < len(dp[with_him]):
                    dp[with_him] = dp[k] + [i]
        return dp[(1 << n) - 1]
