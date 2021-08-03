class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_map = {}
        for idx, group_size in enumerate(groupSizes):
            if group_size not in size_map:
                size_map[group_size] = [[idx]]
            else:
                for group_list in size_map[group_size]:
                    if len(group_list) < group_size:
                        group_list.append(idx)
                        break
                else:
                    # new group list
                    size_map[group_size].append([idx])
        ret = []
        for k, v in list(size_map.items()):
            ret.extend(v)
        return ret
