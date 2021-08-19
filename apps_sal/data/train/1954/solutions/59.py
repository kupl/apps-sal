class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        def convertToNum(people: List[str]) -> int:
            ans = 0
            for skill in people:
                ans |= 1 << dic[skill]
            return ans
        dic = {v: i for (i, v) in enumerate(req_skills)}
        target = (1 << len(req_skills)) - 1
        dp = dict()
        for (i, people_skill) in enumerate(people):
            skill = convertToNum(people_skill)
            temp = dict()
            temp[skill] = [i]
            for key in list(dp.keys()):
                if key != skill:
                    new_skill = key | skill
                    if new_skill not in list(dp.keys()) or len(dp[new_skill]) > len(dp[key]) + 1:
                        t = [v for v in dp[key]]
                        t.append(i)
                        if new_skill not in list(temp.keys()) or len(temp[new_skill]) > len(t):
                            temp[new_skill] = t
            dp.update(temp)
        return dp[target]
