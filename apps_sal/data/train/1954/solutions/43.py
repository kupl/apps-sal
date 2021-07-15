class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
#         res = [''] * 17
#         n = len(req_skills)
#         def dfs(idx, has, path):
#             nonlocal res
#             if idx == n:
#                 res = path
#             elif req_skills[idx] in has:
#                 dfs(idx + 1, has, path)
#             else:
#                 if len(path) + 1 < len(res):
#                     for i, p in enumerate(people):
#                         p = set(p)
#                         if req_skills[idx] in p:
#                             union = p & has
#                             has |= p
#                             dfs(idx + 1, has, path + [i])
#                             has -= p
#                             has |= union
#         dfs(0, set(), [])
#         return res
                        
        
        
        n = len(req_skills)
        key = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p:
                if skill in key:
                    his_skill |= 1 << key[skill]
            for skill_set, need in list(dp.items()):
                with_him = skill_set | his_skill
                if with_him == skill_set: continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]
