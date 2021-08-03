class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        if len(names) <= 1:
            return names

        used = set()

        for p, i in enumerate(names):
            if i not in used:
                used.add(i)
                names[p] = i
            else:
                oldi = i
                k = 0
                while i in used:
                    k += 1
                    i = f'{oldi}({k})'
                used.add(i)
                names[p] = i

        return names
