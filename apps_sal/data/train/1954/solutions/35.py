class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        lrs = len(req_skills)
        skills = collections.defaultdict(list)
        peo_skills = []
        for i, skill in enumerate(people):
            for s in skill:
                skills[s].append(i)
        self.res = [0] * (lrs + 1)

        def dfs(idx, cover, path):
            if idx == lrs:
                self.res = path
            if idx >= lrs:
                return
            if req_skills[idx] in cover:
                dfs(idx + 1, cover, path)
            if len(path) + 1 < len(self.res):
                for p in skills[req_skills[idx]]:
                    p_s = set(people[p])
                    new_cover = cover | p_s
                    dfs(idx + 1, new_cover, path + [p])
        dfs(0, set(), [])
        return self.res
