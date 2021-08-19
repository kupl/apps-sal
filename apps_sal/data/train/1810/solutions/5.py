class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        strs = set()
        new_strs = []
        for name in names:
            if name not in strs:
                strs.add(name)
                new_strs.append(name)
            else:
                i = 1
                while True:
                    new_str = f'{name}({i})'
                    if new_str not in strs:
                        strs.add(new_str)
                        new_strs.append(new_str)
                        break
                    i += 1
        return new_strs
