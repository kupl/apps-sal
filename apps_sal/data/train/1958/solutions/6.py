class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        restrictions = {}

        for unique_id in range(len(groupSizes)):
            group_size = groupSizes[unique_id]
            if group_size in restrictions:
                restrictions[group_size].append(unique_id)
            else:
                restrictions[group_size] = [unique_id]

        res = []

        for group_size in restrictions:
            unique_ids = restrictions[group_size]
            for i in range(0, len(unique_ids), group_size):
                res.append(unique_ids[i:i + group_size])
        return res
