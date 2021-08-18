class Solution:
    from collections import defaultdict

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dic = {req_skills[rs]: 2**rs for rs in range(len(req_skills))}
        dp = defaultdict(list)
        m_pp = []
        for pp in range(len(people)):
            temp = dp.copy()
            res = 0
            for itr_pp in people[pp]:
                res += dic[itr_pp]
            if res != 0:
                temp[res] = [pp]
                for j, v in list(dp.items()):
                    if len(temp[j]) > 0:
                        sum_ = j | res
                        if len(temp[sum_]) == 0 or len(temp[sum_]) > len(temp[j] + [pp]):
                            temp[sum_] = temp[j] + [pp]
                dp = temp
        return dp[2**len(req_skills) - 1]
