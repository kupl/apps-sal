class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        p_skills = [set() for _ in people]
        for (i, p) in enumerate(people):
            p_skills[i] = set(p)
        res = [0] * 17

        def dfs(idx=0, path=[], has=set()):
            nonlocal res
            if idx == len(req_skills):
                res = path
            elif req_skills[idx] in has:
                dfs(idx + 1, path, has)
            elif len(path) + 1 < len(res):
                for (i, p) in enumerate(people):
                    if req_skills[idx] in p_skills[i]:
                        dfs(idx + 1, path + [i], has | p_skills[i])
        dfs()
        return res
