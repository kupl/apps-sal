class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        def fulfill_skills(skills, person):
            remaining_skills = deque()
            for skill in skills:
                if skill not in people[person]:
                    remaining_skills.appendleft(skill)
            return remaining_skills
        has_skill = dict()
        for (person, skills) in enumerate(people):
            for skill in skills:
                experts = has_skill.get(skill, [])
                experts.append(person)
                has_skill[skill] = experts
        rare_skills = [(len(people), skill) for (skill, people) in list(has_skill.items())]
        rare_skills.sort()
        rare_skills = [skill for (_, skill) in rare_skills]
        for i in range(1, 17):
            stack = [(deque(rare_skills), [])]
            while stack:
                (skills, team) = stack.pop()
                if not skills:
                    return team
                if len(team) + 1 > i:
                    continue
                skill = skills[0]
                for person in has_skill[skill]:
                    remaining_skills = fulfill_skills(skills, person)
                    stack.append((remaining_skills, team + [person]))
        return -1
