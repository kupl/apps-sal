class Solution:

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for i in words:
            temp = i
            if len(pattern) == len(temp):
                as1 = {}
                got = []
                found = 1
                for i1 in range(len(temp)):
                    if pattern[i1] not in as1:
                        if temp[i1] in got:
                            found = 0
                            break
                        else:
                            as1[pattern[i1]] = temp[i1]
                            got.append(temp[i1])
                    elif temp[i1] != as1.get(pattern[i1]):
                        found = 0
                        break
                if found == 1:
                    ans.append(temp)
        return ans
