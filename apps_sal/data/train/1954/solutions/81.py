class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        pmasks = []
        for p in people:
            mask = 0
            for skill in p:
                idx = req_skills.index(skill)
                mask ^= 1 << idx
            pmasks.append(mask)
        M = pow(2, len(req_skills)) - 1
        
        @functools.lru_cache(maxsize=None)
        def dfs(mask):
            if mask == M:
                return []
            ret = None
            
            for i, p in enumerate(pmasks):
                if mask|p != mask:
                    ppl = dfs(mask|p)
                    if ppl != None and (not ret or len(ret) > len(ppl) + 1):
                        ret = [i] + ppl
                        #print(i, ppl)
            #print(mask, ret)
            return ret
        
        #print(M, pmasks)
        return dfs(0)
