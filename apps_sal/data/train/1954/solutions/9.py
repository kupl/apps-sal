class Solution:
    # dp
    # bit_manipulation
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # build a dict for skills
        N, skill_dict = len(req_skills), {}
        for i in range(N):
            skill_dict[req_skills[i]] = i
        # what is dp[i] = [], i is the bit expression of skills, value is a list of people with skills which i required
        dp = [list(range(len(people))) for _ in range(1 << N)]
        dp[0] = []

        # loop all people
        for i in range(len(people)):
            # get all skills of ith people
            skill = 0
            for s in people[i]:
                skill |= (1 << skill_dict[s])

            for k, v in enumerate(dp):
                # k is the skills, so new_skill is the new skills when add ith people to this list
                new_skill = k | skill
                # if skills increased and groups has less people, then updat dp
                if new_skill != k and len(v) + 1 < len(dp[new_skill]):
                    dp[new_skill] = v + [i]

        return dp[(1 << N) - 1]



