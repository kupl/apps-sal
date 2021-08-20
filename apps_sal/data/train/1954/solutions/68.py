class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_id_map = {skill: 1 << i for (i, skill) in enumerate(req_skills)}
        ids_indices_map = {0: []}
        for (index, person_skills) in enumerate(people):
            person_ids = 0
            for skill in person_skills:
                person_ids |= skill_id_map[skill]
            new_ids_indices_map = ids_indices_map.copy()
            for (ids, indices) in ids_indices_map.items():
                new_ids = ids | person_ids
                new_indices = indices + [index]
                if len(new_indices) <= len(new_ids_indices_map.get(new_ids, new_indices)):
                    new_ids_indices_map[new_ids] = new_indices
            ids_indices_map = new_ids_indices_map
        return ids_indices_map[2 ** len(req_skills) - 1]
