class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        h = dict()
        ans = []
        for i in names:
            if i not in h:
                h[i] = 1
                ans.append(i)
            else:
                ct = h[i]
                tmp = i + '(' + str(ct) + ')'
                while tmp in h:
                    ct += 1
                    tmp = i + '(' + str(ct) + ')'
                h[tmp] = 1
                ans.append(tmp)
                h[i] = ct
        return ans
