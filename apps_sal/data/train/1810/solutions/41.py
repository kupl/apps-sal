class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = {}
        ans = []

        for i in names:

            if i not in list(d.keys()):
                ans.append(i)
                d[i] = [1, set()]
                continue
            curno, sets = d[i]
            while curno in sets or i + '(' + str(curno) + ')' in list(d.keys()):
                curno += 1
            ans.append(i + '(' + str(curno) + ')')
            d[i + '(' + str(curno) + ')'] = [1, set()]
            d[i][0] = curno + 1
        return ans
