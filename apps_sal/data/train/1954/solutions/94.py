from collections import defaultdict

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        def backtrack(i, people_added, skills_added):
            nonlocal result
            if i == len(req_skills):
                result = list(people_added)
            elif req_skills[i] in skills_added:
                backtrack(i+1, people_added, skills_added)
            else:
                if len(people_added) < len(result) - 1:
                    for k, skills in list(skills_dict.items()):
                        if req_skills[i] in skills:
                            backtrack(i+1, people_added + [k], skills_added | skills)
                            
        result = list(range(len(req_skills)+1))
        skills_dict = {i: set(skills) for i, skills in enumerate(people)}
        backtrack(0, [], set())
        return result

