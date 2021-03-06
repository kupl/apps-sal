from math import inf
from functools import reduce
from operator import or_


def memorized(f):
    memo = {}

    def helper(*arg):
        if arg not in memo:
            memo[arg] = f(*arg)
        return memo[arg]
    return helper


class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        (N, MASK) = (len(people), (1 << len(req_skills)) - 1)
        (skill2id, child) = ({skill: i for (i, skill) in enumerate(req_skills)}, {})
        people = [reduce(operator.or_, (1 << skill2id[skill] for skill in skills), 0) for skills in people]

        @memorized
        def dp(i: int, status: int) -> int:
            if i >= N:
                return 0 if status == MASK else inf
            (not_choose, choose) = (dp(i + 1, status), 1 + dp(i + 1, status | people[i]))
            if not_choose <= choose:
                child[i, status] = (i + 1, status)
                return not_choose
            else:
                child[i, status] = (i + 1, status | people[i])
                return choose
        (i, mask, res) = (-1, 0, [])
        dp(i, mask)
        while mask < MASK:
            if child[i, mask] != (i + 1, mask):
                res.append(i)
            (i, mask) = child[i, mask]
        return res
