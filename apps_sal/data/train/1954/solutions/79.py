class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        L = len(req_skills)
        
        d = {}
        mask = 1
        for i in req_skills:
            d[i] = mask
            mask <<= 1
        
        p = [0] * len(people)
        for i, lst in enumerate(people):
            p[i] += sum([d[j] for j in lst])
            
        print(p)
    
        @functools.lru_cache(None)
        def dp(mask):
            if mask == 2 ** L - 1:
                return []

            smallest = float(\"inf\")
            ret = []
            for i, skills in enumerate(p):
                if mask & skills != skills:
                    tmp = dp(mask | skills)
                    if len(tmp) < smallest:
                        smallest = len(tmp)
                        ret = [i] + tmp
            return ret
        
        return dp(0)
