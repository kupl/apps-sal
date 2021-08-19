class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        l = len(req_skills)
        skill_to_idx = {s: i for (i, s) in enumerate(req_skills)}

        @functools.lru_cache(None)
        def dfs(cur_skill, idx):
            if cur_skill == 2 ** l - 1:
                return ()
            if idx == len(people):
                return None
            cur = 0
            for skill in people[idx]:
                if skill in skill_to_idx and 1 << skill_to_idx[skill] & cur_skill == 0:
                    cur |= 1 << skill_to_idx[skill]
            ret = dfs(cur_skill, idx + 1)
            if cur != 0:
                tmp = dfs(cur_skill | cur, idx + 1)
                if tmp != None and ret != None:
                    ret = min(ret, tuple([idx, *tmp]), key=len)
                elif tmp != None:
                    ret = tuple([idx, *tmp])
            return ret
        ret = dfs(0, 0)
        return ret
