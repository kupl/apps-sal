#skillsets[skillset] = team, is a sufficient team to cover the skillset.
#For each people, update skillsets with all current combinations in skillsets.
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skillid = {skill: i for i, skill in enumerate(req_skills)}
        skillsets = {0: []}
        for i, p in enumerate(people):
            #create people[i]'s skill mask
            skillmask = 0
            for skill in p:
                if skill in skillid:
                    skillmask |= (1 << skillid[skill])
            #combine
            current_skillsets = list(skillsets.keys())
            for skillset in current_skillsets:
                within_i = skillset | skillmask
                if within_i not in skillsets or len(skillsets[within_i]) > len(skillsets[skillset])+1:
                    skillsets[within_i] = skillsets[skillset] + [i]
        c, mult = 0, 1
        for i in range(len(req_skills)):
            c += mult
            mult *= 2
        return skillsets[c]

