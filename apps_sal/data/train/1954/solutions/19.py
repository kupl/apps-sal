class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        peopleLen = len(people)
        skillsLen = len(req_skills)
        maskFull = (1 << skillsLen)-1
        newPeople = []
        for p in people:
            newPeople.append(set(p))
        
        dp = {}
        
        def findPeople(m0, i0):
            if m0 == maskFull:
                return []
            if i0 == peopleLen:
                return None
            if (m0, i0) in dp:
                return dp[(m0, i0)]
            nextM = m0
            for j in range(skillsLen):
                if m0 >> j & 1 == 1:
                    continue
                if req_skills[j] in newPeople[i0]:
                    nextM |= 1 <<j
            ans = None
            if nextM != m0:
                subAns = findPeople(nextM, i0+1)
                if subAns != None:
                    ans = subAns + [i0]
            subAns = findPeople(m0, i0+1)
            if ans == None or subAns != None and len(subAns) < len(ans):
                ans = subAns
            dp[(m0, i0)] = ans
            return ans
        
        return findPeople(0, 0)
