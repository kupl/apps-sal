class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        seen_set = set()
        new_names = []
        for name in names:
            new_name = name
            if new_name in seen_set:
                i = 1
                while new_name in seen_set:
                    new_name = f'{name}({i})'
                    i += 1
            new_names.append(new_name)
            seen_set.add(new_name)
        return new_names
