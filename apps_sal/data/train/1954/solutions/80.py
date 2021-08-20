class Solution:

    def smallestSufficientTeam(self, skills: List[str], people: List[List[str]]) -> List[int]:
        skill2idx = {skill: i for (i, skill) in enumerate(skills)}
        for i in range(len(people)):
            mask = 0
            for skill in people[i]:
                mask |= 1 << skill2idx[skill]
            people[i] = mask
        stop = (1 << len(skills)) - 1

        @lru_cache(None)
        def dfs(i, mask):
            if mask == stop:
                return ()
            if i == len(people):
                return None
            ans1 = dfs(i + 1, mask)
            ans2 = dfs(i + 1, mask | people[i])
            if ans2 is not None:
                ans2 = (i,) + ans2
            if ans1 is None:
                return ans2
            elif ans2 is None:
                return ans1
            else:
                return min(ans1, ans2, key=len)
        return dfs(0, 0)
