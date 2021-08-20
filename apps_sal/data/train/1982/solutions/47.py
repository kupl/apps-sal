from queue import Queue


class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.g = self.build_graph(dislikes)
        self.visited = set()
        self.colors = dict()
        for u in self.g.keys():
            q = Queue()
            q.put(u)
            if u not in self.colors:
                self.colors[u] = 0
            while not q.empty():
                cur = q.get()
                self.visited.add(cur)
                for v in self.g[cur]:
                    if v in self.colors and self.colors[v] == self.colors[cur]:
                        return False
                    if v not in self.visited:
                        self.colors[v] = self.colors[cur] ^ 1
                        self.visited.add(v)
                        q.put(v)
        return True

    def build_graph(self, dislikes):
        g = collections.defaultdict(set)
        for (u, v) in dislikes:
            g[u].add(v)
            g[v].add(u)
        return g
