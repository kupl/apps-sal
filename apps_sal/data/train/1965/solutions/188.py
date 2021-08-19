class UnionFind:

    def __init__(self):
        self.parents = defaultdict(lambda: -1)
        self.ranks = defaultdict(lambda: 1)

    def join(self, a, b):
        (pa, pb) = (self.find(a), self.find(b))
        if pa == pb:
            return False
        if self.ranks[pa] > self.ranks[pb]:
            self.parents[pb] = pa
            self.ranks[pa] += self.ranks[pb]
        else:
            self.parents[pa] = pb
            self.ranks[pb] += self.ranks[pa]
        return True

    def find(self, a):
        if self.parents[a] == -1:
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        def pre_check(person):
            my_edges = [edge for edge in edges if edge[0] in [person, 3]]
            dic = defaultdict(list)
            for (_, a, b) in my_edges:
                dic[a].append(b)
                dic[b].append(a)
            seen = set()

            def dfs(curr):
                if curr in seen:
                    return
                seen.add(curr)
                for nxt in dic[curr]:
                    dfs(nxt)
            dfs(1)
            return len(seen) == n
        if not pre_check(1) or not pre_check(2):
            return -1
        both_edges = [edge for edge in edges if edge[0] == 3]
        a_cnt = sum((edge[0] == 1 for edge in edges))
        b_cnt = sum((edge[0] == 2 for edge in edges))
        uf = UnionFind()
        rid = 0
        for edge in both_edges:
            if not uf.join(edge[1], edge[2]):
                rid += 1
        uniq = set((uf.find(i) for i in range(1, n + 1)))
        uniq = len(uniq)
        return rid + a_cnt - uniq + 1 + b_cnt - uniq + 1
