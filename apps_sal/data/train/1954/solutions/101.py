class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        target = (1<<n)-1
        skills = []
        for p in people:
            mask = 0
            for s in p:
                mask |= 1 << req_skills.index(s)
            skills.append(mask)
        dp = [float('inf')/2 for _ in range(1 << n)]
        pt = [0 for _ in range(1 << n)]
        dp[0] = 0
        for i in range(len(people)):
            k = skills[i]
            if k == 0:
                continue
            for j in range(target+1)[::-1]:
                if dp[j] + 1 < dp[j|k]:
                    dp[j|k] = dp[j]+1
                    pt[j|k] = (j, i) # (parent, current)
        t = target
        ans = []
        while t:
            ans.append(pt[t][1])
            t = pt[t][0]
        return ans
                

