import functools
class Solution():
    def smallestSufficientTeam(self, req_skills, people):
        # 1:14
        # as we know skills are less  we can use bit to represent stage
        # lets use skills acquired statge to be 1
        # bits and dp question
        skills = dict()
        for i, v in enumerate(req_skills):
            skills[v] = i
        n = len(people)
        desiredskills = 2**len(skills)-1
        peopleskills=[]
        for p in people:
            mask=0
            for skill in p:
                mask|=1<<skills[skill]
            peopleskills.append(mask)
            
                
            
        @functools.lru_cache(None)
        def helper(i, teamskills):
            nonlocal n, desiredskills
            ans = float('inf')
            rlist = []
            if teamskills == desiredskills:
                return 0, None
            if i == n:
                return float('inf'), None
            # i will never reach n as answer exists
            # 2 options now
            # either we pick ith person or not
            # if we pick
            newteamskills = teamskills | peopleskills[i]
            
            # for skill in people[i]:
            #     skillpos = skills[skill]
            #     # set this bit to 1 in newpendingskills
            #     # and with zero
            #     newteamskills = newteamskills | (1 << skillpos)

            pickans, picklist = helper(i+1, newteamskills)
            pickans += 1

            if pickans < ans:
                ans = pickans
                rlist = [i]
                if picklist:
                    rlist.extend(picklist)
            pickans, picklist = helper(i+1, teamskills)
            if pickans < ans:
                ans = pickans
                if picklist:
                    rlist = picklist[:]
                else:
                    rlist = None
            return ans, rlist
        return helper(0, 0)[1]
