class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        graph = collections.defaultdict(set)
        for (i, companies) in enumerate(favoriteCompanies):
            for comp in companies:
                graph[comp].add(i)
        ans = []
        for (i, companies) in enumerate(favoriteCompanies):
            groups = None
            for comp in companies:
                if groups is None:
                    groups = set((x for x in graph[comp]))
                else:
                    groups &= graph[comp]
            if len(groups) == 1:
                ans.append(i)
        return ans
