class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        N, M = len(req_skills), len(people)
        NN = 1 << N
        skill2id = {jj: ii for ii, jj in enumerate(req_skills)}
        team = {ii: [] for ii in range(NN)}
        dp = [-1] * NN
        dp[0] = 0

        for ii in range(M):
            idx = 0
            for s in people[ii]:
                if s in skill2id:
                    idx = idx | (1 << skill2id[s])
            for jj in range(NN):
                if dp[jj] < 0:
                    continue
                x = jj | idx
                if dp[x] == -1 or dp[x] > dp[jj] + 1:
                    # print(ii, jj, x, team)
                    dp[x] = dp[jj] + 1
                    team[x] = team[jj].copy()
                    team[x].append(ii)
        # print(team)
        return team[NN - 1]
