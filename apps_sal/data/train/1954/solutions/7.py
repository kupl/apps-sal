from collections import deque


class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        q = deque()
        skill_to_index = {}
        for (i, skill) in enumerate(req_skills):
            skill_to_index[skill] = i
        all_skills = (1 << len(req_skills)) - 1
        people_skills = [0] * len(people)
        dp = {}
        for i in range(len(people)):
            for skill in people[i]:
                people_skills[i] |= 1 << skill_to_index[skill]
            q.appendleft([1 << i, people_skills[i]])
            dp[people_skills[i]] = 1

        def count(bitmask):
            res = []
            for i in range(len(people)):
                if 1 << i & bitmask:
                    res.append(i)
            return res
        while q:
            (bitmask, skills) = q.pop()
            if skills == all_skills:
                return count(bitmask)
            for i in range(len(people)):
                nbitmask = 1 << i | bitmask
                nskills = people_skills[i] | skills
                if nskills not in dp or dp[nskills] > dp[skills] + 1:
                    dp[nskills] = dp[skills] + 1
                    q.appendleft([nbitmask, people_skills[i] | skills])
        return []
