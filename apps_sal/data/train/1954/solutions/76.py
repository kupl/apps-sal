from collections import defaultdict


class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        def backtrack(i, people_added, skills_added):
            nonlocal result
            if i == len(req_skills):
                result = list(people_added)
            elif i in skills_added:
                backtrack(i + 1, people_added, skills_added)
            elif len(people_added) < len(result) - 1:
                for (k, skills_ix) in list(skills_dict.items()):
                    if i in skills_ix:
                        backtrack(i + 1, people_added + [k], skills_added | skills_ix)
        result = list(range(len(req_skills) + 1))
        req_skills_ix_map = {skill: i for (i, skill) in enumerate(req_skills)}
        skills_dict = {i: set([req_skills_ix_map[skill] for skill in skills]) for (i, skills) in enumerate(people)}
        backtrack(0, [], set())
        return result
