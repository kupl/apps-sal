class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = dict()
        self.new_touched = dict()
        self.new_vis_nodes_count = 0

    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:

        for u, v, w in edges:
            self.graph[u].append((v, w))
            self.graph[v].append((u, w))

        nodes_queue = [(0, 0)]
        self.visited[0] = 0
        while len(nodes_queue):
            v_dist, v = heappop(nodes_queue)
            self.visited[v] = v_dist
            for u, w in self.graph[v]:

                # self.new_touched[(v,u)]=max(min(w,M-v_dist),self.new_touched.get((v,u),0))
                self.new_touched[(v, u)] = max(min(w, M - v_dist), self.new_touched.get((v, u), 0))

                if u not in self.visited and M >= v_dist + w + 1:
                    heappush(nodes_queue, (v_dist + w + 1, u))

        res = len(list(self.visited.items()))
        for u, v, w in edges:
            res += min(w, self.new_touched.get((u, v), 0) + self.new_touched.get((v, u), 0))

        return res
