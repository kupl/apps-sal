from functools import reduce
import operator


class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        z = (1 << n) - 1
        rs = {x: 1 << i for (i, x) in enumerate(req_skills)}
        ps = list(map(lambda p: reduce(operator.__or__, map(lambda s: rs[s], p), 0), people))
        d = {0: []}
        for (i, s) in enumerate(ps):
            p = {}
            for x in d:
                y = x | s
                if y not in p or len(d[x]) < len(p[y]):
                    p[y] = d[x] + [i]
            for y in p:
                if y not in d or len(p[y]) < len(d[y]):
                    d[y] = p[y]
        return d[z]
