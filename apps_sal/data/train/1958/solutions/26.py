class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for id, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = [[id]]
            else:
                lastGroup = groups[size][-1]
                if len(lastGroup) != size:
                    groups[size][-1] += [id]
                else:
                    groups[size] += [[id]]
        flatList = []
        for k, v in list(groups.items()):
            flatList += v
        return flatList
