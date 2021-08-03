class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        num_skills, team_queue = len(req_skills), collections.deque()
        bit_map, people_map = {req_skills[i]: i for i in range(num_skills)}, collections.defaultdict(list)
        for i, lst in enumerate(people):
            person_bit = 0
            for l in lst:
                person_bit = person_bit | (1 << bit_map[l])
            for l in lst:
                people_map[bit_map[l]].append((i, person_bit))

        team_queue.append((0, []))
        while team_queue:
            bits, team = team_queue.popleft()
            min_idx = 0
            while min_idx < num_skills and (bits & (1 << min_idx)):
                min_idx += 1
            if min_idx == num_skills:
                return team

            for p, person_bit in people_map[min_idx]:
                team_queue.append((bits | person_bit, team + [p]))

        return []
