class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # Similar to Knapsack problem. First use a binary string to represent a skill set, with target being 2^n-1 (if 3 skills are required, target will be 111).
        # dp[i][j] := min people to reach skill set represented by binary string using first i people
        # dp[0][0] = 0
        # dp[i][j | k] = min(dp[i-1][j | k], dp[i-1][j] + 1), where k is the ith person's skillset.
        # if you have a skillset k of 100 and current j is 001, you can achieve a skillset new j of 100 | 001 = 101. So j of 101 can be achieved either with selecting me which is dp[i-1][j] + 1, or not selecting me - which is equivalent to achieving skillset of j | k with i-1 people, so dp[i-1][j|k]. Now we need to keep a pt (parent child relationship) to later link all the nodes we have traveled to get to the optimal answer dp[n][2^n-1].
        n = len(req_skills)
        target = (1 << n) - 1
        skills = []
        for p in people:
            mask = 0
            for s in p:
                mask |= 1 << req_skills.index(s)
            skills.append(mask)
        dp = [float('inf') for _ in range(1 << n)]
        pt = [0 for _ in range(1 << n)]
        dp[0] = 0
        for i in range(len(people)):
            k = skills[i]
            if k == 0:
                continue
            for j in range(target + 1)[::-1]:
                if dp[j] + 1 < dp[j | k]:
                    dp[j | k] = dp[j] + 1
                    pt[j | k] = (j, i)  # (parent, current)
        t = target
        ans = []
        while t:
            ans.append(pt[t][1])
            t = pt[t][0]
        return ans
