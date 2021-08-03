from collections import defaultdict


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = defaultdict(int)
        for idx, i in enumerate(names):
            suffix = i
            orig = False
            if suffix not in d:
                orig = True
            while suffix in d:
                suffix = i + '(' + str(d[i]) + ')'
                d[i] += 1
            names[idx] = suffix
            if orig:
                d[i] += 1
            else:
                d[suffix] += 1

        return names
