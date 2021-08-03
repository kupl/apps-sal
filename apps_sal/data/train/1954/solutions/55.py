class Solution:

    def rec(self, rs, rdic, people, ret, rett, unis):
        if len(set(unis)) == len(rs):
            if len(ret) < len(rett):
                return ret

        if len(ret) >= len(rett):
            return rett

        for r, v in list(rs.items()):
            if r not in set(unis):
                for p in rdic[r]:
                    rett = self.rec(rs, rdic, people, ret + [p], rett, unis + people[p])
                break
        return rett

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        rdic = {}
        rs = {}
        for r in req_skills:
            rdic[r] = []
            rs[r] = 0

        for i in range(len(people)):
            for r in range(len(people[i])):
                rdic[people[i][r]].append(i)

        rett = [i for i in range(len(people))]
        return self.rec(rs, rdic, people, [], rett, [])
