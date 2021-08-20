from typing import List


class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        exists = {}
        res = []
        for name in names:
            if name not in exists:
                res.append(name)
                exists[name] = 1
            else:
                newName = '{}({})'.format(name, exists[name])
                exists[name] += 1
                while newName in exists:
                    newName = '{}({})'.format(name, exists[name])
                    exists[name] += 1
                exists[newName] = 1
                res.append(newName)
        return res


s = Solution()
