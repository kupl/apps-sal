from collections import defaultdict


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        def backtrack(i, people_added, skills_added):
            nonlocal result
            if i == len(req_skills):
                result = people_added
            elif req_skills[i] in skills_added:
                backtrack(i + 1, people_added, skills_added)
            else:
                if not result or len(people_added) < len(result) - 1:
                    for k in range(len(people)):
                        p = set(people[k])
                        if req_skills[i] in p:
                            union = p & skills_added
                            backtrack(i + 1, people_added + [k], skills_added | p)
                            skills_added |= union
        result = []
        backtrack(0, [], set())
        return result
