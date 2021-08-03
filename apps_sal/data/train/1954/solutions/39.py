class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        from collections import defaultdict

        g = defaultdict(list)

        for i, skills in enumerate(people):
            for s in skills:
                g[s].append(i)

        memo = {}

        def helper(skills, group):
            if not skills:
                return set()

            if tuple(skills) in memo:
                return memo[tuple(skills)]

            new_group = None
            s = list(skills)[0]
            for ind in g[s]:
                if ind in group:
                    continue

                comb = helper(skills - set(people[ind]), group | {ind}) | {ind}
                if not new_group or len(comb) < len(new_group):
                    new_group = comb
            # print(new_group)
            memo[tuple(skills)] = new_group
            return new_group

        return helper(set(req_skills), set())
