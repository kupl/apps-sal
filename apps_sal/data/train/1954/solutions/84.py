class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_id = {skill: i for (i, skill) in enumerate(req_skills)}

        def getSkillSetId(skills):
            res = 0
            for skill in skills:
                if skill in skill_id:
                    res |= 1 << skill_id[skill]
            return res
        req_skills = getSkillSetId(req_skills)
        people = list(map(getSkillSetId, people))

        @functools.lru_cache(None)
        def dfs(req_skills, pid):
            if req_skills == 0:
                return [0, []]
            elif pid == -1:
                return [float('inf'), []]
            else:
                sol1 = dfs(req_skills, pid - 1)
                sol2 = dfs(req_skills & ~people[pid], pid - 1)
                if sol2[0] + 1 < sol1[0]:
                    return [sol2[0] + 1, sol2[1] + [pid]]
                else:
                    return sol1
        return dfs(req_skills, len(people) - 1)[1]

    def smallestSufficientTeam_II(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_id = {skill: idx for (idx, skill) in enumerate(req_skills)}

        def getSkillId(skill_set):
            res = 0
            for skill in skill_set:
                res = res | (1 << skill_id[skill] if skill in skill_id else 0)
            return res
        people = [getSkillId(skills) for skills in people]
        req_skills = getSkillId(req_skills)

        @functools.lru_cache(maxsize=None)
        def dfs(req_skills, pid):
            if req_skills == 0:
                return [0, []]
            elif pid == len(people):
                return [float('inf'), []]
            else:
                sol1 = dfs(req_skills, pid + 1)
                sol2 = dfs(req_skills & ~people[pid], pid + 1)
                if sol2[0] + 1 < sol1[0]:
                    return [sol2[0] + 1, [pid] + sol2[1]]
                else:
                    return sol1
        return dfs(req_skills, 0)[1]
