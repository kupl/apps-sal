class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m = len(req_skills), len(people)
        key = {v: i for i, v in enumerate(req_skills)}
        
        @functools.lru_cache(None)
        def helper(cur = 0):
            if cur == (1 << n) - 1:
                return []
            ans = math.inf
            res = []
            for i, p in enumerate(people):
                his_skill = 0
                for skill in p:
                    if skill in key:
                        his_skill |= 1 << key[skill]
                if his_skill | cur == cur:
                    continue
                temp = helper(cur | his_skill)
                if len(temp) + 1 < ans:
                    res = temp + [i]
                    ans = len(temp) + 1
            return res
        return helper()
