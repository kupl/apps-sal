class Solution:
    # Version 1: Use one dict to store all version numbers
    # TC: O(n), SC: O(n)
    def getFolderNames(self, names: List[str]) -> List[str]:
        version = {}
        ans = []
        for k in names:
            if k not in version:
                ans.append(k)
                version[k] = 1
            else:
                res = k + '(' + str(version[k]) + ')'
                while res in version:
                    version[k] += 1
                    res = k + '(' + str(version[k]) + ')'
                ans.append(res)
                version[res] = 1
        return ans
