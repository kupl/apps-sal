\"\"\"
make a dictionary that is {skill  : people}
while still have skills
   find the rarest skill 
        option- iterate over the dictionary of skills (O(n_skills))
   for each person with the skill:
        add them, then combine them with the smallest Sufficient team from the remaining skills (recursion)
        pick the smallest of these
\"\"\"
from collections import defaultdict

class KeyToSetDict(object):
    def __init__():
        self.dict = {}
        self.sets = []
    
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skills_to_people = defaultdict(list)
        
        people = [set(p) for p in people]
        
        def add_person(i):
            for skill in people[i]:
                skills_to_people[skill].append(i)
                
        for i in range(len(people)):
            add_person(i)
        
        
        def remove_person(i):
            for skill in people[i]:
                skills_to_people[skill].remove(i)
        
        def inner(req_skills):
            if len(req_skills) == 0:
                return []
            
            # find (one of) the rarest skill
            rarest_skill = req_skills[0]
            count = len(skills_to_people[rarest_skill])
            for skill in req_skills[1:]:
                if len(skills_to_people[skill]) <= count:
                    rarest_skill = skill
                    count = len(skills_to_people[skill])

        
            result = []
            min_team_size = len(people)
            
            people_with_skill = skills_to_people[rarest_skill][:]
            for i in people_with_skill:
                remove_person(i)
                sub_req_skills = [x for x in req_skills if x not in set(people[i])]
                remaining_members = inner(sub_req_skills)
                if  len(remaining_members) + 1 <= min_team_size :
                    remaining_members.append(i)
                    result = remaining_members
                    min_team_size = len(result)
                add_person(i)
                    
                
            return result
        
        return inner(req_skills)
