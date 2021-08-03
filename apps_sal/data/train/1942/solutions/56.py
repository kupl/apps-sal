class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        graph = collections.defaultdict(set)
        for i, companies in enumerate(favoriteCompanies):
            for comp in companies:
                graph[comp].add(i)
        ans = []
        for i, companies in enumerate(favoriteCompanies):
            groups = None
            for comp in companies:
                if groups is None:
                    groups = set(x for x in graph[comp])
                else:
                    groups &= graph[comp]
            if len(groups) == 1:
                ans.append(i)
        return ans

        # build trie
#         trie = {}
#         for companies in favoriteCompanies:
#             companies.sort()
#             for c in (companies[i:] for i in range(len(companies))):
#                 node = trie
#                 for e in c:
#                     if e not in node:
#                         node[e] = {'#': 0}
#                     node = node[e]
#                     node['#'] += 1
#         ans = []
#         for i, companies in enumerate(favoriteCompanies):
#             node = trie
#             for c in companies:
#                 node = node[c]
#             if node['#'] == 1: ans.append(i)
#         return ans
