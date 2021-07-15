class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dp = {
            0: []
        }
        
        skill_to_index = {skill: i for i, skill in enumerate(req_skills)}
        for i, skills in enumerate(people):
            mask = 0
            for skill in skills:
                mask |= 1 << (skill_to_index[skill])
            keys = list(dp.keys())
            for filled_req in keys:
                new_filled_req = filled_req | mask
                if (new_filled_req not in dp) or (len(dp[new_filled_req]) > len(dp[filled_req]) + 1):
                    dp[new_filled_req] = dp[filled_req] + [i]
        return dp[(1 << len(req_skills))-1]
