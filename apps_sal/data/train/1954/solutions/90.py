from functools import lru_cache


class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        all_skills = (1 << n) - 1
        max_team = [0] * len(people)

        def construct_mask(skills):
            mask = 0
            for skill in skills:
                mask |= 1 << req_skills.index(skill)
            return mask
        people = [construct_mask(skills) for skills in people]

        @lru_cache(maxsize=None)
        def min_team(idx, skills):
            if skills == all_skills:
                return []
            if idx >= len(people):
                return None
            team = max_team
            for i in range(idx, len(people)):
                temp_mask = skills | people[i]
                if temp_mask == skills:
                    continue
                other_people = min_team(i + 1, temp_mask)
                if other_people is None:
                    continue
                if len(other_people) + 1 < len(team):
                    team = [i] + other_people
            return team
        return min_team(0, 0)
