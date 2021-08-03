class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        n = len(favoriteCompanies)
        f = [set(c) for c in favoriteCompanies]
        for i in range(n):
            for j in range(n):
                if i != j and f[i] & f[j] == f[i]:
                    break
            else:
                ans.append(i)
        return ans
