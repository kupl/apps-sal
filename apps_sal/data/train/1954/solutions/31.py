class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        def fulfill_skills(skills, person):
            remaining_skills = deque()
            for skill in skills:
                if skill not in people[person]:
                    remaining_skills.appendleft(skill)
            return remaining_skills

        # BFS by # of people
        # can reduce expansion by searching rarest skills first

        # map required skills to people
        # has_skill[\"java\"] == a list of people (int index into people) who have that skill
        has_skill = dict()
        for person, skills in enumerate(people):
            for skill in skills:
                experts = has_skill.get(skill, [])
                experts.append(person)
                has_skill[skill] = experts


        # sort skills by rarity
        rare_skills = [(len(people), skill)  for (skill, people) in list(has_skill.items())]
        rare_skills.sort()
        rare_skills = [skill for _, skill in rare_skills]


        # queue holds pairs:
        #   (skills, team)
        q = deque()
        q.append( (deque(rare_skills), []) )
        while q:
            skills, team = q.popleft()
            print((skills, team))
            if not skills:
                return team

            # choose a member to fulfill next rarest skill
            skill = skills[0]
            for person in has_skill[skill]:
                remaining_skills = fulfill_skills(skills, person)
                q.append( (remaining_skills, team + [person]) )


        return -1

