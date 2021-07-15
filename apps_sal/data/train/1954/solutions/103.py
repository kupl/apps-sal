from collections import defaultdict
from functools import lru_cache

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        req_skills = set(req_skills)
        d = {}
        for i, x in enumerate(req_skills):
            d[x] = i
        
        @lru_cache(None)
        def dfs(state, idx):
            if state == 2 ** len(req_skills) - 1:
                return []
            if idx == len(people):
                return [0] * 100
            out = dfs(state, idx + 1)
            new_state = state
            for skill in people[idx]:
                new_state |= 1 << d[skill]
            new = dfs(new_state, idx + 1)
            if len(out) < len(new) + 1:
                return out
            return [idx] + new
        
        return dfs(0, 0)

