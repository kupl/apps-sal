from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        \"\"\"
        find union

        把 pairs 視為 graph edge, 用 find union alg 分群
        找出每個群的 idxes / chars
        個別排序，填回
        \"\"\"
        parents = [i for i in range(len(s))]  # 這邊要用不同的 id，後面才好處理

        def find_parent(v) -> int:
            if parents[v] != v:
                parents[v] = find_parent(parents[v])
            return parents[v]

        # union
        for edge in pairs:
            p1, p2 = find_parent(edge[0]), find_parent(edge[1])
            parents[p1] = p2

        # group idx/char in each group as map
        group_idx_mapping = {}
        group_char_mapping = {}
        for i in range(len(s)):  # for each idx
            group_id = find_parent(i)
            try:
                group_idx_mapping[group_id].append(i)
            except KeyError:
                group_idx_mapping[group_id] = [i]
            try:
                group_char_mapping[group_id].append(s[i])
            except KeyError:
                group_char_mapping[group_id] = [s[i]]

        # sort idx/chars in each group
        ans = [''] * len(s)
        for i in range(len(s)):  # for each group
            if i not in group_idx_mapping:
                continue
            # idxes = sorted(group_idx_mapping[i])
            idxes = group_idx_mapping[i]  # already sorted
            chars = sorted(group_char_mapping[i])
            for j in range(len(idxes)):
                ans[idxes[j]] = chars[j]

        return ''.join(ans)

        # \"\"\"
        # DFS
        # \"\"\"
        # # build graph
        # g = [[] for _ in range(len(s))]
        # for edge in pairs:
        #     g[edge[0]].append(edge[1])
        #     g[edge[1]].append(edge[0])  # bug: 應為 indirected graph
        #
        # # DFS, find components
        # visited = set()
        #
        # def f(i):  # fulfill idexes and chars
        #     if i in visited:
        #         return
        #     else:
        #         visited.add(i)
        #
        #     # visit
        #     idxes.append(i)
        #     chars.append(s[i])
        #
        #     for adj in g[i]:
        #         f(adj)
        #
        # ans = [''] * len(s)
        # for i in range(len(s)):
        #     if i in visited:
        #         continue
        #     idxes = []
        #     chars = []
        #     f(i)
        #
        #     # sort each components
        #     idxes.sort() # bug
        #     chars.sort()
        #
        #     for j in range(len(chars)):
        #         ans[idxes[j]] = chars[j]
        #
        # return ''.join(ans)



