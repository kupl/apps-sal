class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        skill_to_idx = {s: idx for idx, s in enumerate(req_skills)}

        skills = []
        for p in people:
            mask = 0
            for s in p:
                mask |= (1 << skill_to_idx[s])
            skills.append(mask)

        dp = {0: []}
        for i in range(len(people)):
            tmp = dp.copy()
            for s, p in list(dp.items()):
                ns = s | skills[i]
                if ns not in tmp or len(p) + 1 < len(tmp[ns]):
                    tmp[ns] = p + [i]
            dp = tmp

        return dp[(1 << n) - 1]
