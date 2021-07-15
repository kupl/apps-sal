class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        dic = collections.defaultdict(list)
        fc = favoriteCompanies
        for i, p in enumerate(fc):
            for c in p:
                dic[c].append(i)
        n = len(fc)
        counter = [[0] * n for _ in range(n)]
        for l in dic.values():
            for i in range(len(l)):
                for j in range(i + 1, len(l)):
                    counter[l[i]][l[j]] += 1
                    counter[l[j]][l[i]] += 1
        ans = set()
        for i in range(n):
            for j in range(n):
                if counter[i][j] == len(fc[i]):
                    ans.add(i)
                    break
               
        return sorted(set(range(n)) - ans)
