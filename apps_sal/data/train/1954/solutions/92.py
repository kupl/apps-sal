class Solution:
    from collections import defaultdict

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dic = {req_skills[rs]: 2 ** rs for rs in range(len(req_skills))}
        dp = {i: [] for i in range(2 ** len(req_skills))}
        m_pp = []
        for pp in range(len(people)):
            res = 0
            for itr_pp in people[pp]:
                res += dic[itr_pp]
            if res != 0:
                dp[res] = [pp]
                for j in list(dp.keys()):
                    if len(dp[j]) > 0:
                        sum_ = j | res
                        if len(dp[sum_]) == 0 or len(dp[sum_]) > len(dp[j] + [pp]):
                            dp[sum_] = dp[j] + [pp]
        return dp[2 ** len(req_skills) - 1]
