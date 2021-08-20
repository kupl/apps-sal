class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        (ans, suffixNum) = ([], Counter())
        for name in names:
            if name in suffixNum:
                while name + '(' + str(suffixNum[name]) + ')' in suffixNum:
                    suffixNum[name] += 1
                ans.append(name + '(' + str(suffixNum[name]) + ')')
            else:
                ans.append(name)
            suffixNum[ans[-1]] += 1
        return ans
