class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_idx = {s: i for i, s in enumerate(req_skills)}
        n = len(req_skills)
        
        def encode(p):
            res = 0
            for sk in p:
                res |= 1 << skill_idx[sk]
            return res
        
        people_code = [encode(p) for p in people]
        target = (1 << n) - 1
        people_arr = 0
        m = len(people)
        
        
        covers = {0: []}
        for i, pcode in enumerate(people_code):
            for code, people_arr in list(covers.copy().items()):
                new_code = pcode | code
                
                if new_code == code or (new_code in covers and len(people_arr) >= len(covers[new_code])):
                    continue
                covers[new_code] = people_arr + [i]
        return covers[target]
                    
            
        
                    
        
                
            

