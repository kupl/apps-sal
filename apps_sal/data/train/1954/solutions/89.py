from functools import lru_cache


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        ids = {}
        sid = 0
        skills = 0
        for skill in req_skills:
            ids[skill] = sid
            skills = skills | (1 << sid)
            sid += 1

        n = len(people)

        @lru_cache(None)
        def dp(i, left):
            if left == 0:
                return []
            if i == n:
                return None

            a = dp(i + 1, left)

            for s in people[i]:
                if s in ids:
                    j = ids[s]
                    left = (left & ~(1 << j))

            b = dp(i + 1, left)

            if a is not None and b is not None:
                if len(a) < len(b) + 1:
                    return a
                else:
                    return [i] + b

            if a is None and b is None:
                return None

            return ([i] + b) if a is None else a

        return dp(0, skills)
