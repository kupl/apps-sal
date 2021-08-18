class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dic = {req_skills[rs]: 2**rs for rs in range(len(req_skills))}
        dp = [[] for i in range(2**len(req_skills))]
        m_pp = []
        for pp in range(len(people)):
            res = 0
            for itr_pp in people[pp]:
                res += dic[itr_pp]
            if res != 0:
                dp[res] = [pp]
            m_pp.append(res)
        for i in range(len(m_pp)):
            if m_pp[i] == 0:
                continue
            dp[m_pp[i]] = [i]
            for j in range(len(dp)):
                if len(dp[j]) > 0:
                    sum_ = j | m_pp[i]
                    if len(dp[sum_]) == 0 or len(dp[sum_]) > len(dp[j] + [i]):
                        dp[sum_] = dp[j] + [i]

        return dp[-1]
