class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        INT_MAX = 2147483647
        n = len(req_skills)
        pskills = list()
        target = (1 << n) - 1
        dp = [INT_MAX for i in range(target + 1)]
        parent = [list() for i in range(target + 1)]
        umap = dict()
        for i in range(n):
            umap[req_skills[i]] = i
        for p in people:
            mask = 0
            for sk in p:
                mask |= 1 << umap[sk]
            pskills.append(mask)
        dp[0] = 0
        pLen = len(people)
        for i in range(pLen):
            k = pskills[i]
            if k == 0:
                continue
            for j in range(target + 1):
                if dp[j | k] > dp[j] + 1:
                    dp[j | k] = dp[j] + 1
                    parent[j | k] = [j, i]
        t = target
        result = list()
        while t > 0:
            result.append(parent[t][1])
            t = parent[t][0]
        return result
