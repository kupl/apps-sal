class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        company = favoriteCompanies
        company = [set(i) for i in company]
        print(company)

        visited = [False] * len(company)
        res = []
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

        for i in range(len(company)):
            if not visited[i]:
                res.append(i)

        return res
