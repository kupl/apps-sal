import functools


class Solution():
    def smallestSufficientTeam(self, req_skills, people):
        skills = dict()
        for i, v in enumerate(req_skills):
            skills[v] = i
        n = len(people)
        desiredskills = 2**len(skills) - 1
        peopleskills = []
        for p in people:
            mask = 0
            for skill in p:
                mask |= 1 << skills[skill]
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
            newteamskills = teamskills | peopleskills[i]

            pickans, picklist = helper(i + 1, newteamskills)
            pickans += 1

            if pickans < ans:
                ans = pickans
                rlist = [i]
                if picklist:
                    rlist.extend(picklist)
            pickans, picklist = helper(i + 1, teamskills)
            if pickans < ans:
                ans = pickans
                if picklist:
                    rlist = picklist[:]
                else:
                    rlist = None
            return ans, rlist
        return helper(0, 0)[1]
