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
                return 0, []
            if idx == len(people):
                return float('inf'), []
            out = dfs(state, idx + 1)
            new_state = state
            for skill in people[idx]:
                new_state |= 1 << d[skill]
            new = dfs(new_state, idx + 1)
            if out[0] < new[0] + 1:
                return out
            return new[0] + 1, [idx] + new[1]

        return dfs(0, 0)[1]
