class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        if len(names) <= 1:
            return names

        used = set()
        newNames = []

        for name in names:
            if name in used:
                k = 1
                numName = f'{name}({k})'

                while numName in used:
                    k += 1
                    numName = f'{name}({k})'

                used.add(numName)
                newNames.append(numName)

            else:
                used.add(name)
                newNames.append(name)

        return newNames
