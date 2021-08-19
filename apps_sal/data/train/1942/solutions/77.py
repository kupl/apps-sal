class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [set(i) for i in favoriteCompanies]
        visited = [False] * len(favoriteCompanies)
        res = []
        for i in range(len(favoriteCompanies) - 1):
            if visited[i]:
                continue
            else:
                for j in range(i + 1, len(favoriteCompanies)):
                    if favoriteCompanies[i].intersection(favoriteCompanies[j]) == favoriteCompanies[i]:
                        visited[i] = True
                        break
                    elif favoriteCompanies[i].intersection(favoriteCompanies[j]) == favoriteCompanies[j]:
                        visited[j] = True
        for i in range(len(favoriteCompanies)):
            if not visited[i]:
                res.append(i)
        return res
