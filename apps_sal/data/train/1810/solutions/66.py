class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        prefix_counts = dict()
        ret = []
        for name in names:
            if name not in prefix_counts:
                ret.append(name)
                prefix_counts[name] = 0
            else:
                temp_count = prefix_counts[name] + 1
                while f'{name}({temp_count})' in prefix_counts:
                    temp_count += 1
                prefix_counts[name] = temp_count
                new_name = f'{name}({prefix_counts[name]})'
                prefix_counts[new_name] = 0
                ret.append(new_name)
        return list(ret)
