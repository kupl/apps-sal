class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # Use dp and use bit to map the skill
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


#         skills = set(req_skills)
#         res = []
#         def recursive(index,team):
#             if index == len(people):
#                 if set(got.keys()) == skills:res.append(team)
#             else:
#                 for i in range(index,len(people)):
#                     for s in people[i]:
#                         got[s] += 1
#                     recursive(i+1,team+[i])
#                     for s in people[i]:
#                         got[s] -= 1
#                         if got[s] == 0:
#                             del got[s]

#         got = collections.defaultdict(int)
#         recursive(0,[])
#         res.sort(key=lambda x:len(x))
#         return res[0]
