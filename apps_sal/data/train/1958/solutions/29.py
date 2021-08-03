class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = sorted(list(enumerate(groupSizes)), key=lambda x: x[1])
        # return groups
        out = []
        while groups:
            last_group_idx = -groups[-1][1]
            out.append([t[0] for t in groups[last_group_idx:]])
            groups = groups[:last_group_idx]

        return out
