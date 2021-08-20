class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        c = set()
        d = {}
        i = 0
        com = []
        for j in favoriteCompanies:
            cur = set()
            for x in j:
                if x not in d:
                    d[x] = i
                    i += 1
                cur.add(d[x])
            com += [cur]
        ans = []
        for i in range(len(com)):
            flag = False
            for j in range(len(com)):
                if i != j:
                    if com[i].issubset(com[j]):
                        flag = True
                        break
            if not flag:
                ans += [i]
        return ans
