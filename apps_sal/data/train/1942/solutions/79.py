class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        company = favoriteCompanies
        company = [set(i) for i in company]

        visited = [False] * len(company)

        for i in range(len(company) - 1):
            if(visited[i]):
                continue

            root = company[i]
            for j in range(i + 1, len(company)):
                child = company[j]
                if(len(root.intersection(child)) == len(root)):
                    visited[i] = True
                    break

                elif(len(root.intersection(child)) == len(child)):
                    visited[j] = True

        res = []

        for i in range(len(visited)):
            if(visited[i] == False):
                res.append(i)

        return res
