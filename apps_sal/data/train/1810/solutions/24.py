# 1487. Making File Names Unique

def get_names (names):
    next_index = {}
    ans = []

    for name in names:
        if name not in next_index:
            next_index[name] = 1
            ans.append (name)
        else:
            index = next_index[name]
            while f'{name}({index})' in next_index:
                index += 1
            # found index
            next_index[name] = index
            new_name = f'{name}({index})'
            assert new_name not in next_index
            next_index[new_name] = 1
            ans.append (new_name)

    return ans


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        return get_names(names)
