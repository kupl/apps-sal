class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        g = collections.defaultdict(set)
        self.parent = [i for i in range(len(favoriteCompanies))]
        for i, companies in enumerate(favoriteCompanies):
            g[i] = set(companies)
        for i in range(len(favoriteCompanies)):
            for j in range(i+1,len(favoriteCompanies)):
                a,b = self.find(i),self.find(j)
                if a != b:
                    if g[a] >= g[b]:
                        self.parent[b] = a
                    elif g[b] > g[a]:
                        self.parent[a] = b
        res = set()
        for i in range(len(favoriteCompanies)):
            res.add(self.find(i))
        return sorted(res)
        
    def find(self,i):
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

