class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill2num = {}
        for (i, skill) in enumerate(req_skills):
            skill2num[skill] = i
        p2s = [0] * len(people)
        for (i, p) in enumerate(people):
            skills = 0
            for skill in p:
                if skill in skill2num:
                    skills += 1 << skill2num[skill]
            p2s[i] = skills
        N = len(req_skills)
        dp = [1000000000] * (1 << N)
        dp[0] = 0
        ans = [[] for i in range(1 << N)]
        for i in range(len(people)):
            dp2 = dp.copy()
            for skill in range(1 << N):
                new_skills = skill | p2s[i]
                if dp2[new_skills] > dp[skill] + 1:
                    dp2[new_skills] = dp[skill] + 1
                    ans[new_skills] = list(ans[skill])
                    ans[new_skills].append(i)
            dp = dp2
        return ans[(1 << N) - 1]
