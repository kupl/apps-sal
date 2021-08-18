class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        mapping = {v: i for i, v in enumerate(req_skills)}
        record = {0: []}
        for i, p in enumerate(people):
            skills = 0
            for s in p:
                if s in mapping:
                    skills |= 1 << mapping[s]
            for v, l in list(record.items()):
                withThis = v | skills
                if withThis == v:
                    continue
                if withThis not in record or len(record[withThis]) > len(l) + 1:
                    record[withThis] = l + [i]
        return record[(1 << len(req_skills)) - 1]
