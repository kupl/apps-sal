from functools import lru_cache
from collections import defaultdict
import math


class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        mp = defaultdict(int)
        for (i, skill) in enumerate(req_skills):
            mp[skill] = i
        skills = []
        for p in people:
            mask = 0
            for skill in p:
                mask |= 1 << mp[skill]
            skills.append(mask)

        @lru_cache(None)
        def search(i: int, required: int) -> int:
            if required == 0:
                return 0
            if i == len(people):
                return math.inf
            return min(search(i + 1, required), 1 + search(i + 1, required ^ required & skills[i]))
        ans = []
        required = (1 << len(req_skills)) - 1
        for i in range(len(people)):
            if search(i + 1, required) > 1 + search(i + 1, required ^ required & skills[i]):
                ans.append(i)
                required ^= required & skills[i]
        return ans
