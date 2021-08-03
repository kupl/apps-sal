class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        allneed = (1 << len(req_skills)) - 1

        stoi = {}
        for i, s in enumerate(req_skills):
            stoi[s] = 1 << i

        def serialize(arr):
            res = 0
            for s in arr:
                res = res | stoi[s]
            return res

        ppl = []
        for i, p in enumerate(people):
            ppl.append(serialize(p))

        tempmax = [0] * (len(req_skills) + 1)

        @lru_cache(None)
        def helper(needed):
            if needed == 0:
                return []
            shortest = tempmax
            for i, person in enumerate(ppl):
                if (person & needed) > 0:
                    sofar = [i] + helper((person ^ allneed) & needed)
                    if (len(sofar) < len(shortest)):
                        shortest = sofar
            return shortest

        return helper(allneed)
