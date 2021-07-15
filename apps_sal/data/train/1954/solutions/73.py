class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        res = {}
        res[0] = set()
        skill_map = {v: i for i, v in enumerate(req_skills)}
        print(skill_map)
        
        for p, skills in enumerate(people):
            curr_skill = 0
            for skill in skills:
                curr_skill |= (1 << skill_map[skill])
            # print(curr_skill)
            
            nr = {}
            for s, t in res.items():
                k = curr_skill | s
                nt = t | {p}
                if k not in res:
                    if k not in nr or len(nr[k]) > len(nt): nr[k] = nt
                elif len(res[k]) > len(nt):
                    res[k] = nt
            res.update(nr)
            # print(res, nr)
        
        return list(res[(1 << n) - 1])
