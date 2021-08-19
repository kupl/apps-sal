class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skills = []
        for p in people:
            cur = 0
            for skill in p:
                for (i, req_skill) in enumerate(req_skills):
                    if skill == req_skill:
                        cur |= 1 << i
            skills.append(cur)
        n = len(req_skills)
        target = (1 << n) - 1
        dp = [1000000 for i in range(target + 1)]
        dp[0] = 0
        parent = [0] * (target + 1)
        for i in range(len(people)):
            k = skills[i]
            if k == 0:
                continue
            for j in reversed(list(range(target))):
                if dp[j | k] > dp[j] + 1:
                    dp[j | k] = dp[j] + 1
                    parent[j | k] = (j, i)
        t = target
        result = []
        while t:
            result.append(parent[t][1])
            t = parent[t][0]
        return result
