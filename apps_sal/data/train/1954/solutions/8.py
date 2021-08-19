class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        def convertToNum(people: List[str]) -> int:
            ans = 0
            for skill in people:
                ans |= 1 << dic[skill]
            return ans
        dic = {v: i for (i, v) in enumerate(req_skills)}
        dp = {v: [] for v in range(1, 1 << len(req_skills))}
        for (i, people_skill) in enumerate(people):
            skill = convertToNum(people_skill)
            dp[skill] = [i]
            for key in list(dp.keys()):
                if key != skill and len(dp[key]) > 0 and (i not in dp[key]):
                    new_skill = key | skill
                    if len(dp[new_skill]) > len(dp[key]) + 1 or len(dp[new_skill]) == 0:
                        temp = [v for v in dp[key]]
                        temp.append(i)
                        dp[new_skill] = temp
        return dp[(1 << len(req_skills)) - 1]
