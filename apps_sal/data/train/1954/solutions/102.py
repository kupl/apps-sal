class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        s2i = {}
        for i, skill in enumerate(req_skills):
            s2i[skill] = i

        n = len(people)
        p2n = [0] * n
        for i, p in enumerate(people):
            temp = 0
            for skill in p:
                temp |= 1 << s2i[skill]
            p2n[i] = temp

        goal = (1 << len(req_skills)) - 1
        dp = [sys.maxsize] * (goal + 1)
        dp[0] = 0
        saves = [[] for i in range(goal + 1)]

        for i in range(n):
            skill = p2n[i]
            for skillset in range(goal + 1):
                new_skill = skillset | skill
                if dp[new_skill] > dp[skillset] + 1:
                    dp[new_skill] = dp[skillset] + 1
                    saves[new_skill] = list(saves[skillset])
                    saves[new_skill].append(i)

        return saves[goal]
