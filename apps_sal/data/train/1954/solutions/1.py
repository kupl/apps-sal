class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skillsMap = {s: i for i, s in enumerate(req_skills)}
        peopleSkills = collections.defaultdict(set)
        for i, p in enumerate(people):
            for s in p:
                peopleSkills[skillsMap[s]].add(i)
        n = len(req_skills)

        memo = {}
        res = []

        self.dfs(1 << n, memo, peopleSkills, res, n, people, skillsMap)
        return memo[1 << n]

    def dfs(self, state, memo, peopleSkills, res, n, people, skillsMap):
        # print(bin(state)[1:])
        if state == 2 ** (n + 1) - 1:
            return []

        if state in memo:
            return memo[state]

        currState = list(bin(state)[3:])
        mini = float('inf')
        ans = []
        i = currState.index('0')
        for p in peopleSkills[i]:
            for s in people[p]:
                currState[skillsMap[s]] = '1'

            nextState = int('1' + ''.join(currState), 2)
            # print(bin(state), currState, p, nextState)
            temp = self.dfs(nextState, memo, peopleSkills, res, n, people, skillsMap)
            currState = list(bin(state)[3:])
            # print(p, state, nextState, temp)
            if len(temp) < mini:
                mini = len(temp)
                ans = [p] + temp
        # print(ans)
        memo[state] = ans
        return ans
