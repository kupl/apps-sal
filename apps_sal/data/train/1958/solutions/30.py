from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        all_groups = list()
        assignments = defaultdict(list)

        for i, size in enumerate(groupSizes):
            assignments[size].append(i)

        return [people[i:i + size] for size, people in list(assignments.items()) for i in range(0, len(people), size)]
