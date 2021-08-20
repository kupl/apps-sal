class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        result = []
        for (index, size) in enumerate(groupSizes):
            groups[size].append(index)
            if len(groups[size]) == size:
                result.append(groups.pop(size))
        return result
