class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        map = Counter()
        ans = []
        for s in names:
            if map[s] == 0:
                ans.append(s)
                map[s] += 1
            else:
                while map[s + '(' + str(map[s]) + ')'] != 0:
                    map[s] += 1
                map[s + '(' + str(map[s]) + ')'] += 1
                ans.append(s + '(' + str(map[s]) + ')')
        return ans
